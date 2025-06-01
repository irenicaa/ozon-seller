import datetime
from dataclasses import dataclass
from typing import Optional

from .common import credentials, request_api, datetime_field, renamed_field
from .common.data_class_json_mixin import DataClassJsonMixin


# Request


@dataclass
class PostingAdditionalFields(DataClassJsonMixin):
    analytics_data: Optional[bool] = False
    barcodes: Optional[bool] = False
    financial_data: Optional[bool] = False
    translit: Optional[bool] = False


@dataclass
class PostingFBSData(DataClassJsonMixin):
    posting_number: str
    with_: Optional[PostingAdditionalFields] = \
        renamed_field.optional_renamed_field(PostingAdditionalFields, "with")


# Response


@dataclass
class GetPostingFBSDataResponseRequirements(DataClassJsonMixin):
    products_requiring_gtd: Optional[list[int]]
    products_requiring_country: Optional[list[int]]
    products_requiring_mandatory_mark: Optional[list[int]]
    products_requiring_rnpt: Optional[list[int]]


@dataclass
class GetPostingFBSDataResponseDimensions(DataClassJsonMixin):
    height: str
    length: str
    weight: str
    width: str


@dataclass
class GetPostingFBSDataResponseProduct(DataClassJsonMixin):
    dimensions: GetPostingFBSDataResponseDimensions
    mandatory_mark: list[str]
    name: str
    offer_id: str
    price: str
    quantity: int
    sku: int
    currency_code: str


@dataclass
class GetPostingFBSDataResponseExemplarProductInfo(DataClassJsonMixin):
    mandatory_mark: str
    gtd: str
    is_gtd_absent: bool
    rnpt: str
    is_rnpt_absent: bool


@dataclass
class GetPostingFBSDataResponseExemplarProduct(DataClassJsonMixin):
    exemplars: list[GetPostingFBSDataResponseExemplarProductInfo]
    sku: int


@dataclass
class GetPostingFBSDataResponseProductExemplars(DataClassJsonMixin):
    products: list[GetPostingFBSDataResponseExemplarProduct]


@dataclass
class GetPostingFBSDataResponseFinancialPicking(DataClassJsonMixin):
    amount: float
    tag: str
    moment: datetime.datetime = datetime_field.datetime_field()


@dataclass
class GetPostingFBSDataResponseFinancialDataServices(DataClassJsonMixin):
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


@dataclass
class GetPostingFBSDataResponseDataProduct(DataClassJsonMixin):
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


@dataclass
class GetPostingFBSDataResponseFinancialData(DataClassJsonMixin):
    posting_services: GetPostingFBSDataResponseFinancialDataServices
    products: list[GetPostingFBSDataResponseDataProduct]


@dataclass
class GetPostingFBSDataResponseDeliveryMethod(DataClassJsonMixin):
    id: int
    name: str
    tpl_provider: str
    tpl_provider_id: int
    warehouse: str
    warehouse_id: int


@dataclass
class GetPostingFBSDataResponseAddress(DataClassJsonMixin):
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


@dataclass
class GetPostingFBSDataResponseCustomer(DataClassJsonMixin):
    address: GetPostingFBSDataResponseAddress
    customer_email: str
    customer_id: int
    name: str
    phone: str


@dataclass
class GetPostingFBSDataResponseCourier(DataClassJsonMixin):
    car_model: str
    car_number: str
    name: str
    phone: str


@dataclass
class GetPostingFBSDataResponseCancellation(DataClassJsonMixin):
    affect_cancellation_rating: bool
    cancel_reason: str
    cancel_reason_id: int
    cancellation_initiator: str
    cancellation_type: str
    cancelled_after_ship: bool


@dataclass
class GetPostingFBSDataResponseBarcodes(DataClassJsonMixin):
    lower_barcode: str
    upper_barcode: str


@dataclass
class GetPostingFBSDatatResponseAnalyticsData(DataClassJsonMixin):
    city: str
    is_premium: bool
    payment_type_group_name: str
    region: str
    tpl_provider: str
    tpl_provider_id: int
    warehouse: str
    warehouse_id: int
    delivery_date_begin: Optional[datetime.datetime] = \
        datetime_field.optional_datetime_field()


@dataclass
class GetPostingFBSDataResponseAddressee(DataClassJsonMixin):
    name: str
    phone: str


@dataclass
class GetPostingFBSDataResponseAdditionalDataItem(DataClassJsonMixin):
    key: str
    value: str


@dataclass
class GetPostingFBSDataResponseResult(DataClassJsonMixin):
    additional_data: Optional[list[GetPostingFBSDataResponseAdditionalDataItem]]
    addressee: Optional[GetPostingFBSDataResponseAddressee]
    analytics_data: Optional[GetPostingFBSDatatResponseAnalyticsData]
    barcodes: Optional[GetPostingFBSDataResponseBarcodes]
    cancellation: Optional[GetPostingFBSDataResponseCancellation]
    courier: Optional[GetPostingFBSDataResponseCourier]
    customer: Optional[GetPostingFBSDataResponseCustomer]
    delivery_method: Optional[GetPostingFBSDataResponseDeliveryMethod]
    delivery_price: str
    financial_data: Optional[GetPostingFBSDataResponseFinancialData]
    is_express: bool
    order_id: int
    order_number: str
    posting_number: str
    product_exemplars: Optional[GetPostingFBSDataResponseProductExemplars]
    products: list[GetPostingFBSDataResponseProduct]
    provider_status: str
    requirements: Optional[GetPostingFBSDataResponseRequirements]
    status: str
    tpl_integration_type: str
    tracking_number: str
    delivering_date: Optional[datetime.datetime] = \
        datetime_field.optional_datetime_field()
    in_process_at: Optional[datetime.datetime] = \
        datetime_field.optional_datetime_field()
    shipment_date: Optional[datetime.datetime] = \
        datetime_field.optional_datetime_field()


@dataclass
class GetPostingFBSDataResponseResultWrapper(DataClassJsonMixin):
    result: GetPostingFBSDataResponseResult


def get_posting_fbs_data(
    credentials: credentials.Credentials,
    data: PostingFBSData,
) -> GetPostingFBSDataResponseResultWrapper:
    return request_api.request_api_json(
        "POST",
        "/v3/posting/fbs/get",
        credentials,
        data,
        response_cls=GetPostingFBSDataResponseResultWrapper,
    )
