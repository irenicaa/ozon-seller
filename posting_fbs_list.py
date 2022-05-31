from dataclasses import dataclass, field
from typing import Optional
import datetime

from dataclasses_json import dataclass_json, Undefined, config, CatchAll
from marshmallow import fields

import request_api
import credentials

def parse_datetime(value):
    if value is None:
        return None
    elif isinstance(value, str):
        return datetime.datetime.fromisoformat(value)
    elif isinstance(value, datetime.datetime):
        return value
    else:
        raise RuntimeError('unsopported time for a datetime field')

# Request

@dataclass_json
@dataclass
class GetFbsPostingWithParams:
    analytics_data: Optional[bool] = False
    barcodes: Optional[bool] = False
    financial_data: Optional[bool] = False
    translit: Optional[bool] = False

@dataclass_json
@dataclass
class GetFbsPostingListRequestFilter:
    delivery_method_id:  Optional[list[int]] = None
    order_id: Optional[int] = None
    provider_id: Optional[list[int]] = None
    since:  Optional[datetime.datetime] = field(
        metadata=config(
            decoder=datetime.datetime.fromisoformat,
            mm_field=fields.DateTime(format='iso'),
        ),
        default=None,
    )
    to:  Optional[datetime.datetime] = field(
        metadata=config(
            decoder=datetime.datetime.fromisoformat,
            mm_field=fields.DateTime(format='iso'),
        ),
        default=None,
    )
    status:  Optional[str] = None
    warehouse_id:  Optional[list[int]] = None

@dataclass_json
@dataclass
class GetFbsPostingListRequest:
    dir: Optional[str] = 'ASC'
    filter: Optional[GetFbsPostingListRequestFilter] = None
    limit: Optional[int] = None
    offset: Optional[int] = None
    with_: Optional[GetFbsPostingWithParams] = field(metadata=config(field_name="with"), default=None)

# Request

@dataclass_json
@dataclass
class FbsPostingRequirements:
    products_requiring_gtd: Optional[list[int]]
    products_requiring_country: Optional[list[int]]
    products_requiring_mandatory_mark: Optional[list[int]]
    products_requiring_rnpt: Optional[list[int]]

@dataclass_json
@dataclass
class PostingProductDetail:
    mandatory_mark: list[str]
    name: str
    offer_id: str
    price: str
    quantity: int
    sku: int
    currency_code: str


@dataclass_json
@dataclass
class ProductPicking:
    amount: float
    moment: datetime.datetime = field(
        metadata=config(
            decoder=datetime.datetime.fromisoformat,
            mm_field=fields.DateTime(format='iso'),
        ),
    )
    tag: str

@dataclass_json
@dataclass
class PostingFinancialDataServices:
    marketplace_service_item_deliv_to_customer: float
    marketplace_service_item_direct_flow_trans: float
    marketplace_service_item_dropoff_ff: float
    marketplace_service_item_dropoff_pvz: float
    marketplace_service_item_dropoff_sc: float
    marketplace_service_item_fulfillment: float
    marketplace_service_item_pickup: float
    marketplace_service_item_return_after_deliv_to_customer: float
    marketplace_service_item_return_flow_trans: float
    marketplace_service_item_return_not_deliv_to_customer: float
    marketplace_service_item_return_part_goods_customer: float

@dataclass_json
@dataclass
class PostingFinancialDataProduct:
    actions: list[str]
    client_price: str
    commission_amount: float
    commission_percent: int
    item_services: PostingFinancialDataServices
    old_price: float
    payout: float
    picking: ProductPicking
    price: float
    product_id: int
    quantity: int
    total_discount_percent: float
    total_discount_value: float

@dataclass_json
@dataclass
class PostingFinancialData:
    posting_services: PostingFinancialDataServices
    products: list[PostingFinancialDataProduct]

@dataclass_json
@dataclass
class DeliveryMethod:
    id: int
    name: str
    tpl_provider: str
    tpl_provider_id: int
    warehouse: str
    warehouse_id: int

@dataclass_json
@dataclass
class Address:
    address_tail: str
    city: str
    comment: str
    country: str
    district: str
    latitude: float
    longitude: float
    provider_pvz_code: str
    pvz_code: int
    region: str
    zip_code: str

@dataclass_json
@dataclass
class Customer:
    address: Address
    customer_email: str
    customer_id: int
    name: str
    phone: str

@dataclass_json
@dataclass
class Cancellation:
    affect_cancellation_rating: bool
    cancel_reason: str
    cancel_reason_id: int
    cancellation_initiator: str
    cancellation_type: str
    cancelled_after_ship: bool

@dataclass_json
@dataclass
class Barcodes:
    lower_barcode: str
    upper_barcode: str

@dataclass_json
@dataclass
class AnalyticsData:
    city: str
    delivery_date_begin: Optional[datetime.datetime] = field(
        metadata=config(
            decoder=datetime.datetime.fromisoformat,
            mm_field=fields.DateTime(format='iso'),
        ),
    )
    is_premium: bool
    payment_type_group_name: str
    region: str
    tpl_provider: str
    tpl_provider_id: int
    warehouse: str
    warehouse_id: int

@dataclass_json
@dataclass
class Addressee:
    mame: str
    phone: str

@dataclass_json
@dataclass
class GetFbsPostingListResponsePosting:
    addressee: Optional[Addressee]
    analytics_data: Optional[AnalyticsData]
    barcodes: Optional[Barcodes]
    cancellation: Optional[Cancellation]
    customer: Optional[Customer]
    delivering_date: Optional[datetime.datetime] = field(
        metadata=config(
            decoder=parse_datetime,
            mm_field=fields.DateTime(format='iso', allow_none=True),
        ),
    )
    delivery_method: Optional[DeliveryMethod]
    financial_data: Optional[PostingFinancialData]
    in_process_at: Optional[datetime.datetime] = field(
        metadata=config(
            decoder=parse_datetime,
            mm_field=fields.DateTime(format='iso'),
        ),
    )
    is_express: bool
    order_id: int
    order_number: str
    posting_number: str
    products: list[PostingProductDetail]
    requirements: Optional[FbsPostingRequirements]
    shipment_date: datetime.datetime = field(
        metadata=config(
            decoder=parse_datetime,
            mm_field=fields.DateTime(format='iso', allow_none=True),
        ),
    )
    status: str
    tpl_integration_type: str
    tracking_number: str

@dataclass_json
@dataclass
class GetFbsPostingListResponseResult:
    has_next: bool
    postings: list[GetFbsPostingListResponsePosting]


@dataclass_json
@dataclass
class GetFbsPostingListResponseResultWrapper:
    result: GetFbsPostingListResponseResult

def get_posting_fbs_list(
    credentials: credentials.Credentials,
    data: GetFbsPostingListRequest,
) -> GetFbsPostingListResponseResultWrapper:
    response = request_api.request_api_raw(
        'POST',
        '/v3/posting/fbs/list',
        credentials,
        data.to_json(),
    )
    return GetFbsPostingListResponseResultWrapper.schema().loads(response)
