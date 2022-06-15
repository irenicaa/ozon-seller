from dataclasses import dataclass, field
from typing import Optional, Generator
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
class PostingFBSData:
    posting_number: str
    with_: Optional[PostingAdditionalFields] = field(
        default=None,
        metadata=config(field_name="with"),
    )

# Response

@dataclass_json
@dataclass
class GetPostingFBSDataResponseRequirements:
    products_requiring_gtd: Optional[list[int]]
    products_requiring_country: Optional[list[int]]
    products_requiring_mandatory_mark: Optional[list[int]]
    products_requiring_rnpt: Optional[list[int]]

@dataclass_json
@dataclass
class GetPostingFBSDataResponseDimensions:
    height: str
    length: str
    weight: str
    width: str

@dataclass_json
@dataclass
class GetPostingFBSDataResponseProduct:
    dimensions: GetPostingFBSDataResponseDimensions
    mandatory_mark: list[str]
    name: str
    offer_id: str
    price: str
    quantity: int
    sku: int
    currency_code: str

@dataclass_json
@dataclass
class GetPostingFBSDataResponseExemplarProductInfo:
    mandatory_mark: str
    gtd: str
    is_gtd_absent: bool
    rnpt: str
    is_rnpt_absent: bool

@dataclass_json
@dataclass
class GetPostingFBSDataResponseExemplarProduct:
    exemplars: list[GetPostingFBSDataResponseExemplarProductInfo]
    sku: int

@dataclass_json
@dataclass
class GetPostingFBSDataResponseProductExemplars:
    products: list[GetPostingFBSDataResponseExemplarProduct]

@dataclass_json
@dataclass
class GetPostingFBSDataResponseFinancialPicking:
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
class GetPostingFBSDataResponseFinancialDataServices:
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
class GetPostingFBSDataResponseDataProduct:
    actions: list[str]
    client_price: str
    commission_amount: float
    commission_percent: int
    item_services: GetPostingFBSDataResponseFinancialDataServices
    old_price: float
    payout: float
    picking: GetPostingFBSDataResponseFinancialPicking
    price: float
    product_id: int
    quantity: int
    total_discount_percent: float
    total_discount_value: float

@dataclass_json
@dataclass
class GetPostingFBSDataResponseFinancialData:
    posting_services: GetPostingFBSDataResponseFinancialDataServices
    products: list[GetPostingFBSDataResponseDataProduct]

@dataclass_json
@dataclass
class GetPostingFBSDataResponseDeliveryMethod:
    id: int
    name: str
    tpl_provider: str
    tpl_provider_id: int
    warehouse: str
    warehouse_id: int

@dataclass_json
@dataclass
class GetPostingFBSDataResponseAddress:
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
class GetPostingFBSDataResponseCustomer:
    address: GetPostingFBSDataResponseAddress
    customer_email: str
    customer_id: int
    name: str
    phone: str

@dataclass_json
@dataclass
class GetPostingFBSDataResponseCourier:
    car_model: str
    car_number: str
    name: str
    phone: str

@dataclass_json
@dataclass
class GetPostingFBSDataResponseCancellation:
    affect_cancellation_rating: bool
    cancel_reason: str
    cancel_reason_id: int
    cancellation_initiator: str
    cancellation_type: str
    cancelled_after_ship: bool

@dataclass_json
@dataclass
class GetPostingFBSDataResponseBarcodes:
    lower_barcode: str
    upper_barcode: str

@dataclass_json
@dataclass
class GetPostingFBSDatatResponseAnalyticsData:
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
class GetPostingFBSDataResponseAddressee:
    name: str
    phone: str

@dataclass_json
@dataclass
class GetPostingFBSDataResponseAdditionalDataItem:
    key: str
    value: str

@dataclass_json
@dataclass
class GetPostingFBSDataResponseResult:
    additional_data: Optional[list[GetPostingFBSDataResponseAdditionalDataItem]]
    addressee: Optional[GetPostingFBSDataResponseAddressee]
    analytics_data: Optional[GetPostingFBSDatatResponseAnalyticsData]
    barcodes: Optional[GetPostingFBSDataResponseBarcodes]
    cancellation: Optional[GetPostingFBSDataResponseCancellation]
    courier: Optional[GetPostingFBSDataResponseCourier]
    customer: Optional[GetPostingFBSDataResponseCustomer]
    delivering_date: Optional[datetime.datetime] = field(
        metadata=config(
            decoder=parse_datetime,
            mm_field=fields.DateTime(format='iso', allow_none=True),
        ),
    )
    delivery_method: Optional[GetPostingFBSDataResponseDeliveryMethod]
    delivery_price: str
    financial_data: Optional[GetPostingFBSDataResponseFinancialData]
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
    product_exemplars: Optional[GetPostingFBSDataResponseProductExemplars]
    products: list[GetPostingFBSDataResponseProduct]
    provider_status: str
    requirements: Optional[GetPostingFBSDataResponseRequirements]
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
class GetPostingFBSDataResponseResultWrapper:
    result: GetPostingFBSDataResponseResult

def get_posting_fbs_data(
    credentials: credentials.Credentials,
    data: PostingFBSData,
) -> GetPostingFBSDataResponseResultWrapper:
    response = request_api.request_api_raw(
        'POST',
        '/v3/posting/fbs/get',
        credentials,
        data.to_json(),
    )
    return GetPostingFBSDataResponseResultWrapper.schema().loads(response)
