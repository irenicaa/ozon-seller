from dataclasses import dataclass, field
from typing import Optional
import datetime

from dataclasses_json import dataclass_json, Undefined, config, CatchAll
from marshmallow import fields

import request_api
import credentials
import returns_fbs

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
class PostingAdditionalFields:
    analytics_data: Optional[bool] = False
    barcodes: Optional[bool] = False
    financial_data: Optional[bool] = False
    translit: Optional[bool] = False

@dataclass_json
@dataclass
class GetPostingFBSListFilter:
    delivery_method_id: Optional[list[int]] = None
    order_id: Optional[int] = None
    provider_id: Optional[list[int]] = None
    since: Optional[datetime.datetime] = field(
        metadata=config(encoder=returns_fbs.format_datetime),
        default=None,
    )
    to: Optional[datetime.datetime] = field(
        metadata=config(encoder=returns_fbs.format_datetime),
        default=None,
    )
    status: Optional[str] = None
    warehouse_id: Optional[list[int]] = None

@dataclass_json
@dataclass
class PaginatedGetPostingFBSListFilter:
    filter: Optional[GetPostingFBSListFilter] = None
    dir: Optional[str] = 'ASC'
    limit: Optional[int] = None
    offset: Optional[int] = None
    with_: Optional[PostingAdditionalFields] = field(
        default=None,
        metadata=config(field_name="with"),
    )

# Response

@dataclass_json
@dataclass
class GetPostingFBSListResponseRequirements:
    products_requiring_gtd: Optional[list[int]]
    products_requiring_country: Optional[list[int]]
    products_requiring_mandatory_mark: Optional[list[int]]
    products_requiring_rnpt: Optional[list[int]]

@dataclass_json
@dataclass
class GetPostingFBSListResponseProduct:
    mandatory_mark: list[str]
    name: str
    offer_id: str
    price: str
    quantity: int
    sku: int
    currency_code: str

@dataclass_json
@dataclass
class GetPostingFBSListResponsePicking:
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
class GetPostingFBSListResponseFinancialDataServices:
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
class GetPostingFBSListResponseFinancialDataProduct:
    actions: list[str]
    client_price: str
    commission_amount: float
    commission_percent: int
    item_services: GetPostingFBSListResponseFinancialDataServices
    old_price: float
    payout: float
    picking: GetPostingFBSListResponsePicking
    price: float
    product_id: int
    quantity: int
    total_discount_percent: float
    total_discount_value: float

@dataclass_json
@dataclass
class GetPostingFBSListResponseFinancialData:
    posting_services: GetPostingFBSListResponseFinancialDataServices
    products: list[GetPostingFBSListResponseFinancialDataProduct]

@dataclass_json
@dataclass
class GetPostingFBSListResponseDeliveryMethod:
    id: int
    name: str
    tpl_provider: str
    tpl_provider_id: int
    warehouse: str
    warehouse_id: int

@dataclass_json
@dataclass
class GetPostingFBSListResponseAddress:
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
class GetPostingFBSListResponseCustomer:
    address: GetPostingFBSListResponseAddress
    customer_email: str
    customer_id: int
    name: str
    phone: str

@dataclass_json
@dataclass
class GetPostingFBSListResponseCancellation:
    affect_cancellation_rating: bool
    cancel_reason: str
    cancel_reason_id: int
    cancellation_initiator: str
    cancellation_type: str
    cancelled_after_ship: bool

@dataclass_json
@dataclass
class GetPostingFBSListResponseBarcodes:
    lower_barcode: str
    upper_barcode: str

@dataclass_json
@dataclass
class GetPostingFBSListResponseAnalyticsData:
    city: str
    delivery_date_begin: Optional[datetime.datetime] = field(
        metadata=config(
            decoder=parse_datetime,
            mm_field=fields.DateTime(format='iso', allow_none=True),
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
class GetPostingFBSListResponseAddressee:
    name: str
    phone: str

@dataclass_json
@dataclass
class GetPostingFBSListResponsePosting:
    addressee: Optional[GetPostingFBSListResponseAddressee]
    analytics_data: Optional[GetPostingFBSListResponseAnalyticsData]
    barcodes: Optional[GetPostingFBSListResponseBarcodes]
    cancellation: Optional[GetPostingFBSListResponseCancellation]
    customer: Optional[GetPostingFBSListResponseCustomer]
    delivering_date: Optional[datetime.datetime] = field(
        metadata=config(
            decoder=parse_datetime,
            mm_field=fields.DateTime(format='iso', allow_none=True),
        ),
    )
    delivery_method: Optional[GetPostingFBSListResponseDeliveryMethod]
    financial_data: Optional[GetPostingFBSListResponseFinancialData]
    in_process_at: Optional[datetime.datetime] = field(
        metadata=config(
            decoder=parse_datetime,
            mm_field=fields.DateTime(format='iso', allow_none=True),
        ),
    )
    is_express: bool
    order_id: int
    order_number: str
    posting_number: str
    products: list[GetPostingFBSListResponseProduct]
    requirements: Optional[GetPostingFBSListResponseRequirements]
    shipment_date: Optional[datetime.datetime] = field(
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
class GetPostingFBSListResponseResult:
    postings: list[GetPostingFBSListResponsePosting]
    has_next: bool

@dataclass_json
@dataclass
class GetPostingFBSListResponseResultWrapper:
    result: GetPostingFBSListResponseResult

def get_posting_fbs_list(
    credentials: credentials.Credentials,
    data: PaginatedGetPostingFBSListFilter,
) -> GetPostingFBSListResponseResultWrapper:
    response = request_api.request_api_raw(
        'POST',
        '/v3/posting/fbs/list',
        credentials,
        data.to_json(),
    )
    return GetPostingFBSListResponseResultWrapper.schema().loads(response)
