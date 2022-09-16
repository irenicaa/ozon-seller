import datetime
from dataclasses import dataclass, field
from typing import Generator, Optional

from dataclasses_json import CatchAll, Undefined, config, dataclass_json
from marshmallow import fields

from .common import credentials, request_api

# Request


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class ItemPriceData:
    auto_action_enabled: Optional[str] = "UNKNOWN"
    min_price: Optional[str] = None
    offer_id: Optional[str] = None
    old_price: Optional[str] = None
    price: Optional[str] = None
    product_id: Optional[int] = None


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class PricesData:
    prices: Optional[list[ItemPriceData]] = None


# Response


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetProductImportPriceResponseError:
    code: str
    message: str


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetProductImportPriceResponseResult:
    errors: list[GetProductImportPriceResponseError]
    offer_id: str
    product_id: int
    updated: bool


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetProductImportPriceResponseResultWrapper:
    result: list[GetProductImportPriceResponseResult]


def set_product_import_price(
    credentials: credentials.Credentials,
    data: ItemPriceData,
) -> GetProductImportPriceResponseResultWrapper:
    return request_api.request_api_json(
        "POST",
        "/v1/product/import/prices",
        credentials,
        data,
        response_cls=GetProductImportPriceResponseResultWrapper,
    )
