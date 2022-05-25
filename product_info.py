from dataclasses import dataclass, field
from typing import Optional
import datetime

from dataclasses_json import dataclass_json, Undefined, config, CatchAll
from marshmallow import fields

import request_api
import credentials
import returns_fbs

# Request

@dataclass_json
@dataclass
class ProductData:
    offer_id: str  = ''
    product_id: Optional[int] = None
    sku: Optional[int] = None

# Response

@dataclass_json(undefined=Undefined.INCLUDE)
@dataclass
class Property:
    properties: CatchAll

# TODO: property name*
@dataclass_json
@dataclass
class ItemError:
    code: str
    state: str
    level: str
    description: str
    field: str
    attribute_id: str
    attribute_name: str
    optional_description_elements: Property

@dataclass_json
@dataclass
class ProductStatus:
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
    item_errors: list[ItemError]
    state_updated_at: datetime.datetime = \
        field(metadata=config(decoder=datetime.datetime.fromisoformat, mm_field= fields.DateTime(format='iso')))

@dataclass_json
@dataclass
class GetProductInfoResponseVisibilityDetails:
    active_product: bool
    has_price: bool
    has_stock: bool

@dataclass_json
@dataclass
class GetProductInfoResponseStock:
    coming: int
    present: int
    reserved: int

@dataclass_json
@dataclass
class GetProductInfoResponseSource:
    is_enabled: bool
    sku: int
    source: str

@dataclass_json
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
    created_at: datetime.datetime = \
        field(metadata=config(decoder=datetime.datetime.fromisoformat, mm_field=fields.DateTime(format='iso')))
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
    status: ProductStatus
    sources: list[GetProductInfoResponseSource]
    stocks: GetProductInfoResponseStock
    vat: str
    visibility_details: GetProductInfoResponseVisibilityDetails
    visible: bool
    volume_weight: float
