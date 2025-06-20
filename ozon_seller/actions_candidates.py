from dataclasses import dataclass
from typing import Generator, Optional

from .common import credentials, request_api
from .common.data_class_json_mixin import DataClassJsonMixin


# Request


@dataclass
class PaginatedCandidatesForActions(DataClassJsonMixin):
    action_id: Optional[float] = None
    limit: Optional[float] = None
    offset: Optional[float] = None


# Response


@dataclass
class GetActionsCandidatesResponseProducts(DataClassJsonMixin):
    id: float
    price: float
    action_price: float
    max_action_price: float
    add_mode: str
    min_stock: float
    stock: float


@dataclass
class GetActionsCandidatesResponseResult(DataClassJsonMixin):
    products: list[GetActionsCandidatesResponseProducts]
    total: float


@dataclass
class GetActionsCandidatesResponseResultWrapper(DataClassJsonMixin):
    result: GetActionsCandidatesResponseResult


def get_actions_candidates(
    credentials: credentials.Credentials,
    data: PaginatedCandidatesForActions,
) -> GetActionsCandidatesResponseResultWrapper:
    return request_api.request_api_json(
        "POST",
        "/v1/actions/candidates",
        credentials,
        data,
        response_cls=GetActionsCandidatesResponseResultWrapper,
    )


def get_actions_candidates_iterative(
    credentials: credentials.Credentials,
    data: PaginatedCandidatesForActions,
) -> Generator[GetActionsCandidatesResponseResultWrapper, None, None]:
    while True:
        products = get_actions_candidates(credentials, data)
        if products.result.products == []:
            break

        yield products

        data.offset += data.limit
