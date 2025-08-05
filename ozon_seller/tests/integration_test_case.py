from dataclasses import dataclass
from typing import Union, Callable, Any, Optional
from collections.abc import Iterator

from . import common
from . import qualified_name
from . import load_test_case
from .test_server_endpoint import TestServerEndpoint
from .base_test_case import BaseTestCase, primary_field
from ..common import credentials
from ..common import data_class_json_mixin
from ..common import http_error
from ..common import error_response


@dataclass
class IntegrationTestCase(BaseTestCase): # type: ignore[misc]
    request_credentials: credentials.Credentials
    request_data: Optional[data_class_json_mixin.DataClassJsonMixin]
    expected_method: str
    expected_endpoint: str
    requester: Union[
        Callable[[credentials.Credentials, Any], Any],
        Callable[[credentials.Credentials], Any],
    ] = primary_field()
    response_cls: Optional[type[data_class_json_mixin.DataClassJsonMixin]] = None
    step_count: int = 1
    expected_response_items: Optional[list[data_class_json_mixin.DataClassJsonMixin]] = None
    expected_exception: Optional[http_error.HTTPError[error_response.ErrorResponse]] = None

    def validate_modules(self) -> None:
        request_module = qualified_name.get_last_module(self.request_data) \
            if self.request_data is not None \
            else None
        response_module = qualified_name.get_last_module(self.response_cls) \
            if self.response_cls is not None \
            else None
        if (
            request_module is not None
            and response_module is not None
            and request_module != response_module
        ):
            raise RuntimeError(
                "different modules for the request and response: " +
                    f"{request_module} and {response_module}, respectively",
            )

        for item_index, item in enumerate(self.expected_response_items or []):
            item_module = qualified_name.get_last_module(item)
            if item_module not in (request_module, response_module):
                raise RuntimeError(
                    f"unexpected module {item_module} " +
                        f"for the expected response item #{item_index}; " +
                        f"expected {request_module or response_module}",
                )

    def validate_iterative_mode(self) -> None:
        if self.step_count < 1:
            raise RuntimeError("step count must be greater than zero")
        elif self.step_count > 1 and self.expected_response_items is None:
            raise RuntimeError(
                "expected response items are not provided " +
                    "for the test case with multiple steps",
            )

    def make_endpoint(self, step_index: int) -> TestServerEndpoint:
        test_case_kind = f"{common.FULL_TEST_CASE_KIND}_step_{step_index + 1}" \
            if self.step_count > 1 \
            else common.FULL_TEST_CASE_KIND

        expected_request_json = load_test_case.load_test_case(test_case_kind, self.request_data) \
            if self.request_data is not None \
            else None

        if self.response_cls is not None:
            response_type = "application/json"
            response_data = load_test_case.load_test_case(test_case_kind, self.response_cls)
        else:
            response_type = "text/plain"
            response_data = "text-response-data"

        return TestServerEndpoint(
            expected_method=self.expected_method,
            expected_endpoint=self.expected_endpoint,
            expected_credentials=common.TEST_EXPECTED_CREDENTIALS,
            expected_request_json=expected_request_json,
            provided_response_type=response_type,
            provided_response_data=response_data,
        )

    def make_expected_response(self, endpoints: list[TestServerEndpoint]) -> Any:
        if self.expected_response_items is not None:
            return self.expected_response_items

        try:
            response_data = endpoints[0].provided_response_data
        except IndexError:
            raise RuntimeError(
                "unable to determine the response data: " +
                    "the number of endpoints is not equal to one",
            )

        return self.response_cls.schema().loads(response_data) \
            if self.response_cls is not None \
            else response_data.encode("utf-8")

    def call_requester(self) -> Any:
        requester_args = (self.request_credentials, self.request_data) \
            if self.request_data is not None \
            else (self.request_credentials,)
        response = self.requester(*requester_args) # type: ignore[arg-type]
        return list(response) if isinstance(response, Iterator) else response
