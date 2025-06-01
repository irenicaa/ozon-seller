from dataclasses import dataclass
from typing import Optional

from .common import credentials, request_api
from .common.data_class_json_mixin import DataClassJsonMixin


# Request


@dataclass
class ItemPriceData(DataClassJsonMixin):
    auto_action_enabled: Optional[str] = "UNKNOWN"
    min_price: Optional[str] = None
    offer_id: Optional[str] = None
    old_price: Optional[str] = None
    price: Optional[str] = None
    product_id: Optional[int] = None


@dataclass
class PricesData(DataClassJsonMixin):
    prices: Optional[list[ItemPriceData]] = None


# Response


@dataclass
class GetProductImportPriceResponseError(DataClassJsonMixin):
    code: str
    message: str


@dataclass
class GetProductImportPriceResponseResult(DataClassJsonMixin):
    errors: list[GetProductImportPriceResponseError]
    offer_id: str
    product_id: int
    updated: bool


@dataclass
class GetProductImportPriceResponseResultWrapper(DataClassJsonMixin):
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
