from dataclasses import dataclass
from typing import Optional

from .common import credentials, request_api
from .common.data_class_json_mixin import DataClassJsonMixin


# Request


@dataclass
class ProductData(DataClassJsonMixin):
    offer_id: Optional[str] = None
    product_id: Optional[int] = None
    stock: Optional[int] = None
    warehouse_id: Optional[int] = None


@dataclass
class StocksData(DataClassJsonMixin):
    stocks: Optional[list[ProductData]] = None


# Response


@dataclass
class SetProductStocksResponseResult(DataClassJsonMixin):
    offer_id: str
    product_id: int
    updated: bool
    warehouse_id: int


@dataclass
class SetProductStocksResponseResultWrapper(DataClassJsonMixin):
    result: list[SetProductStocksResponseResult]


def set_stocks(
    credentials: credentials.Credentials,
    data: StocksData,
) -> SetProductStocksResponseResultWrapper:
    return request_api.request_api_json(
        "POST",
        "/v2/products/stocks",
        credentials,
        data,
        response_cls=SetProductStocksResponseResultWrapper,
    )
