import datetime
from dataclasses import dataclass, field
from typing import Optional

from dataclasses_json import CatchAll, Undefined, config, dataclass_json
from marshmallow import fields

from . import credentials, request_api

# Request


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class ProductData:
    offer_id: Optional[str] = None
    product_id: Optional[int] = None
    sku: Optional[int] = None


# Response


@dataclass_json(undefined=Undefined.INCLUDE)
@dataclass
class GetProductInfoResponseOptionalDescriptionElements:
    properties: CatchAll


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetProductInfoResponseItemError:
    code: str
    state: str
    level: str
    description: str
    field: str
    attribute_id: str
    attribute_name: str
    optional_description_elements: GetProductInfoResponseOptionalDescriptionElements


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetProductInfoResponseVisibilityDetails:
    active_product: bool
    has_price: bool
    has_stock: bool


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetProductInfoResponseStocks:
    coming: int
    present: int
    reserved: int


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetProductInfoResponseSource:
    is_enabled: bool
    sku: int
    source: str


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetProductInfoResponseStatus:
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
    state_updated_at: datetime.datetime = field(
        metadata=config(
            decoder=datetime.datetime.fromisoformat,
            mm_field=fields.DateTime(format="iso"),
        ),
    )


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetProductInfoResponseCommissions:
    delivery_amount: float
    min_value: float
    percent: float
    return_amount: float
    sale_schema: str
    value: float


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetProductInfoResponseResult:
    barcode: str
    buybox_price: str
    category_id: int
    color_image: str
    commissions: list[GetProductInfoResponseCommissions]
    created_at: datetime.datetime = field(
        metadata=config(
            decoder=datetime.datetime.fromisoformat,
            mm_field=fields.DateTime(format="iso"),
        ),
    )
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


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetProductInfoResponseResultWrapper:
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
