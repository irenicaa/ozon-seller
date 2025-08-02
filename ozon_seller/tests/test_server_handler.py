from __future__ import annotations
from http.server import BaseHTTPRequestHandler
import json
import http

from .test_server_endpoint import TestServerEndpoint
from ..common import credentials
from ..common import error_response


class TestServerHandler(BaseHTTPRequestHandler):
    _endpoints: list[TestServerEndpoint]

    @staticmethod
    def create(endpoints: list[TestServerEndpoint]) -> type[TestServerHandler]:
        class _CustomTestServerHandler(TestServerHandler):
            pass

        _CustomTestServerHandler._endpoints = endpoints

        return _CustomTestServerHandler

    def do_REQUEST(self) -> None:
        try:
            current_endpoint = self._endpoints.pop(0)
        except IndexError:
            self._write_error_response(create_error_response(http.HTTPStatus.INTERNAL_SERVER_ERROR))
            return

        if (
            self.command != current_endpoint.expected_method
            or self.path != current_endpoint.expected_endpoint
        ):
            self._write_error_response(create_error_response(http.HTTPStatus.NOT_FOUND))
            return

        actual_credentials = credentials.Credentials(
            client_id=self.headers.get(credentials.CLIENT_ID_HEADER_KEY, ""),
            api_key=self.headers.get(credentials.API_KEY_HEADER_KEY, ""),
        )
        if actual_credentials != current_endpoint.expected_credentials:
            self._write_error_response(create_error_response(http.HTTPStatus.UNAUTHORIZED))
            return

        if current_endpoint.expected_request_json is not None:
            actual_request_length = int(self.headers.get("Content-Length", 0))
            actual_request_json = self.rfile.read(actual_request_length)
            if not _are_equal_as_json(
                actual_request_json,
                current_endpoint.expected_request_json.encode("utf-8"),
            ):
                self._write_error_response(create_error_response(http.HTTPStatus.BAD_REQUEST))
                return

        self._write_response(
            status_code=200,
            response_type=current_endpoint.provided_response_type,
            response_data=current_endpoint.provided_response_data,
        )

    # proxy all the methods to `do_REQUEST()`
    do_GET = do_HEAD = do_POST = do_PUT = do_DELETE = do_PATCH = do_REQUEST

    def _write_response(self, status_code: int, response_type: str, response_data: str) -> None:
        self.send_response(status_code)
        self.send_header("Content-Type", response_type)
        self.send_header("Content-Length", str(len(response_data)))
        self.end_headers()

        self.wfile.write(response_data.encode("utf-8"))

    def _write_error_response(self, error_response: error_response.ErrorResponse) -> None:
        self._write_response(
            status_code=error_response.code if error_response.code is not None else 500,
            response_type="application/json",
            response_data=error_response.to_json(),
        )


def create_error_response(http_status: http.HTTPStatus) -> error_response.ErrorResponse:
    return error_response.ErrorResponse(
        code=http_status.value,
        message=http_status.phrase,
        details=None,
    )


def _are_equal_as_json(json_one: bytes, json_two: bytes) -> bool:
    try:
        return bool(json.loads(json_one) == json.loads(json_two))
    except json.JSONDecodeError:
        return False
