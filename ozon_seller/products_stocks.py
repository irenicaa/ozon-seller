import datetime
from dataclasses import dataclass, field
from typing import Optional

from dataclasses_json import CatchAll, Undefined, config, dataclass_json
from marshmallow import fields

from .common import credentials, request_api

# Request


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class ProductData:
    offer_id: Optional[str] = None
    product_id: Optional[int] = None
    stock: Optional[int] = None
    warehouse_id: Optional[int] = None


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class StocksData:
    stocks: Optional[list[ProductData]] = None


# Response


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class SetProductStocksResponseResult:
    offer_id: str
    product_id: int
    updated: bool
    warehouse_id: int



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class SetProductStocksResponseResultWrapper:
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
