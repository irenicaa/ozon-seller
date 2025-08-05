import datetime
from dataclasses import dataclass
from typing import Optional

from dataclasses_json import Undefined, CatchAll, config

from .common import credentials, request_api, datetime_field
from .common.data_class_json_mixin import DataClassJsonMixin


# Request


@dataclass
class ProductData(DataClassJsonMixin):
    offer_id: Optional[str] = None
    product_id: Optional[int] = None
    sku: Optional[int] = None


# Response


@dataclass
class GetProductInfoResponseOptionalDescriptionElements(DataClassJsonMixin): # type: ignore[misc]
    dataclass_json_config = \
        config(undefined=Undefined.INCLUDE)["dataclasses_json"] # type: ignore[assignment]

    properties: CatchAll # type: ignore[type-arg]


@dataclass
class GetProductInfoResponseItemError(DataClassJsonMixin):
    code: str
    state: str
    level: str
    description: str
    field: str
    attribute_id: str
    attribute_name: str
    optional_description_elements: GetProductInfoResponseOptionalDescriptionElements


@dataclass
class GetProductInfoResponseVisibilityDetails(DataClassJsonMixin):
    active_product: bool
    has_price: bool
    has_stock: bool


@dataclass
class GetProductInfoResponseStocks(DataClassJsonMixin):
    coming: int
    present: int
    reserved: int


@dataclass
class GetProductInfoResponseSource(DataClassJsonMixin):
    is_enabled: bool
    sku: int
    source: str


@dataclass
class GetProductInfoResponseStatus(DataClassJsonMixin):
    state: str
    state_failed: str
    moderate_status: str
    decline_reasons: list[str]
    validation_state: str
    state_name: str
    state_description: str
    is_failed: bool
    is_created: bool
    state_tooltip: str
    item_errors: list[GetProductInfoResponseItemError]
    state_updated_at: datetime.datetime = datetime_field.datetime_field()


@dataclass
class GetProductInfoResponseCommissions(DataClassJsonMixin):
    delivery_amount: float
    min_value: float
    percent: float
    return_amount: float
    sale_schema: str
    value: float


@dataclass
class GetProductInfoResponseResult(DataClassJsonMixin):
    barcode: str
    buybox_price: str
    category_id: int
    color_image: str
    commissions: list[GetProductInfoResponseCommissions]
    fbo_sku: int
    fbs_sku: int
    id: int
    images: list[str]
    primary_image: str
    images360: list[str]
    is_prepayment: bool
    is_prepayment_allowed: bool
    marketing_price: str
    min_ozon_price: str
    min_price: str
    name: str
    offer_id: str
    old_price: str
    premium_price: str
    price: str
    price_index: str
    recommended_price: str
    status: GetProductInfoResponseStatus
    sources: list[GetProductInfoResponseSource]
    stocks: GetProductInfoResponseStocks
    vat: str
    visibility_details: GetProductInfoResponseVisibilityDetails
    visible: bool
    volume_weight: float
    created_at: datetime.datetime = datetime_field.datetime_field()


@dataclass
class GetProductInfoResponseResultWrapper(DataClassJsonMixin):
    result: GetProductInfoResponseResult


def get_product_info(
    credentials: credentials.Credentials,
    data: ProductData,
) -> GetProductInfoResponseResultWrapper:
    return request_api.request_api_json(
        "POST",
        "/v2/product/info",
        credentials,
        data,
        response_cls=GetProductInfoResponseResultWrapper,
    )
