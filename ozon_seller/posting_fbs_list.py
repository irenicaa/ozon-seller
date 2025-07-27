import datetime
from dataclasses import dataclass
from typing import Iterator, Optional

from .common import (
    credentials,
    request_api,
    datetime_field,
    renamed_field,
    make_iterative,
)
from .common.data_class_json_mixin import DataClassJsonMixin


# Request


@dataclass
class PostingAdditionalFields(DataClassJsonMixin):
    analytics_data: Optional[bool] = False
    barcodes: Optional[bool] = False
    financial_data: Optional[bool] = False
    translit: Optional[bool] = False


@dataclass
class GetPostingFBSListFilter(DataClassJsonMixin):
    delivery_method_id: Optional[list[int]] = None
    order_id: Optional[int] = None
    provider_id: Optional[list[int]] = None
    status: Optional[str] = None
    warehouse_id: Optional[list[int]] = None
    since: Optional[datetime.datetime] = \
        datetime_field.optional_datetime_field()
    to: Optional[datetime.datetime] = datetime_field.optional_datetime_field()


@dataclass
class PaginatedGetPostingFBSListFilter(DataClassJsonMixin):
    filter: Optional[GetPostingFBSListFilter] = None
    dir: Optional[str] = "ASC"
    limit: Optional[int] = None
    offset: Optional[int] = None
    with_: Optional[PostingAdditionalFields] = \
        renamed_field.optional_renamed_field(PostingAdditionalFields, "with")


# Response


@dataclass
class GetPostingFBSListResponseRequirements(DataClassJsonMixin):
    products_requiring_gtd: Optional[list[int]]
    products_requiring_country: Optional[list[int]]
    products_requiring_mandatory_mark: Optional[list[int]]
    products_requiring_rnpt: Optional[list[int]]


@dataclass
class GetPostingFBSListResponseProduct(DataClassJsonMixin):
    mandatory_mark: list[str]
    name: str
    offer_id: str
    price: str
    quantity: int
    sku: int
    currency_code: str


@dataclass
class GetPostingFBSListResponsePicking(DataClassJsonMixin):
    amount: float
    tag: str
    moment: datetime.datetime = datetime_field.datetime_field()


@dataclass
class GetPostingFBSListResponseFinancialDataServices(DataClassJsonMixin):
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
class GetPostingFBSListResponseFinancialDataProduct(DataClassJsonMixin):
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


@dataclass
class GetPostingFBSListResponseFinancialData(DataClassJsonMixin):
    posting_services: GetPostingFBSListResponseFinancialDataServices
    products: list[GetPostingFBSListResponseFinancialDataProduct]


@dataclass
class GetPostingFBSListResponseDeliveryMethod(DataClassJsonMixin):
    id: int
    name: str
    tpl_provider: str
    tpl_provider_id: int
    warehouse: str
    warehouse_id: int


@dataclass
class GetPostingFBSListResponseAddress(DataClassJsonMixin):
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
class GetPostingFBSListResponseCustomer(DataClassJsonMixin):
    address: GetPostingFBSListResponseAddress
    customer_email: str
    customer_id: int
    name: str
    phone: str


@dataclass
class GetPostingFBSListResponseCancellation(DataClassJsonMixin):
    affect_cancellation_rating: bool
    cancel_reason: str
    cancel_reason_id: int
    cancellation_initiator: str
    cancellation_type: str
    cancelled_after_ship: bool


@dataclass
class GetPostingFBSListResponseBarcodes(DataClassJsonMixin):
    lower_barcode: str
    upper_barcode: str


@dataclass
class GetPostingFBSListResponseAnalyticsData(DataClassJsonMixin):
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
class GetPostingFBSListResponseAddressee(DataClassJsonMixin):
    name: str
    phone: str


@dataclass
class GetPostingFBSListResponsePosting(DataClassJsonMixin):
    addressee: Optional[GetPostingFBSListResponseAddressee]
    analytics_data: Optional[GetPostingFBSListResponseAnalyticsData]
    barcodes: Optional[GetPostingFBSListResponseBarcodes]
    cancellation: Optional[GetPostingFBSListResponseCancellation]
    customer: Optional[GetPostingFBSListResponseCustomer]
    delivery_method: Optional[GetPostingFBSListResponseDeliveryMethod]
    financial_data: Optional[GetPostingFBSListResponseFinancialData]
    is_express: bool
    order_id: int
    order_number: str
    posting_number: str
    products: list[GetPostingFBSListResponseProduct]
    requirements: Optional[GetPostingFBSListResponseRequirements]
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
class GetPostingFBSListResponseResult(DataClassJsonMixin):
    postings: list[GetPostingFBSListResponsePosting]
    has_next: bool


@dataclass
class GetPostingFBSListResponseResultWrapper(DataClassJsonMixin):
    result: GetPostingFBSListResponseResult


def get_posting_fbs_list(
    credentials: credentials.Credentials,
    data: PaginatedGetPostingFBSListFilter,
) -> GetPostingFBSListResponseResultWrapper:
    return request_api.request_api_json(
        "POST",
        "/v3/posting/fbs/list",
        credentials,
        data,
        response_cls=GetPostingFBSListResponseResultWrapper,
    )


def get_posting_fbs_list_iterative(
    credentials: credentials.Credentials,
    data: PaginatedGetPostingFBSListFilter,
) -> Iterator[GetPostingFBSListResponsePosting]:
    return make_iterative.make_iterative_via_offset(
        request=data,
        requester=lambda: get_posting_fbs_list(credentials, data),
        extract_response_items=lambda response: response.result.postings,
    )
