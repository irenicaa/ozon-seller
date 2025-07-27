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
    financial_data: Optional[bool] = False


@dataclass
class GetPostingFBOListFilter(DataClassJsonMixin):
    since: Optional[datetime.datetime] = \
        datetime_field.optional_datetime_field()
    to: Optional[datetime.datetime] = datetime_field.optional_datetime_field()
    status: Optional[str] = None


@dataclass
class PaginatedGetPostingFBOListFilter(DataClassJsonMixin):
    filter: Optional[GetPostingFBOListFilter] = None
    dir: Optional[str] = "ASC"
    translit: Optional[bool] = False
    limit: Optional[int] = None
    offset: Optional[int] = None
    with_: Optional[PostingAdditionalFields] = \
        renamed_field.optional_renamed_field(PostingAdditionalFields, "with")


# Response


@dataclass
class GetPostingFBOListResponseProduct(DataClassJsonMixin):
    digital_codes: list[str]
    name: str
    offer_id: str
    price: str
    quantity: int
    sku: int


@dataclass
class GetPostingFBOListResponsePicking(DataClassJsonMixin):
    amount: float
    tag: str
    moment: datetime.datetime = datetime_field.datetime_field()


@dataclass
class GetPostingFBOListResponseFinancialDataServices(DataClassJsonMixin):
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
class GetPostingFBOListResponseFinancialDataProduct(DataClassJsonMixin):
    actions: list[str]
    client_price: str
    commission_amount: float
    commission_percent: int
    item_services: GetPostingFBOListResponseFinancialDataServices
    old_price: float
    payout: float
    picking: GetPostingFBOListResponsePicking
    price: float
    product_id: int
    quantity: int
    total_discount_percent: float
    total_discount_value: float


@dataclass
class GetPostingFBOListResponseFinancialData(DataClassJsonMixin):
    posting_services: GetPostingFBOListResponseFinancialDataServices
    products: list[GetPostingFBOListResponseFinancialDataProduct]


@dataclass
class GetPostingFBOListResponseAnalyticsData(DataClassJsonMixin):
    city: str
    delivery_type: str
    is_legal: bool
    is_premium: bool
    payment_type_group_name: str
    region: str
    warehouse_id: int
    warehouse_name: str


@dataclass
class GetPostingFBOAdditionalDataItem(DataClassJsonMixin):
    key: str
    value: str


@dataclass
class GetPostingFBOListResponseResult(DataClassJsonMixin):
    additional_data: list[GetPostingFBOAdditionalDataItem]
    analytics_data: Optional[GetPostingFBOListResponseAnalyticsData]
    cancel_reason_id: int
    financial_data: Optional[GetPostingFBOListResponseFinancialData]
    order_id: int
    order_number: str
    posting_number: str
    products: list[GetPostingFBOListResponseProduct]
    status: str
    created_at: Optional[datetime.datetime] = \
        datetime_field.optional_datetime_field()
    in_process_at: Optional[datetime.datetime] = \
        datetime_field.optional_datetime_field()


@dataclass
class GetPostingFBOListResponseResultWrapper(DataClassJsonMixin):
    result: list[GetPostingFBOListResponseResult]


def get_posting_fbo_list(
    credentials: credentials.Credentials,
    data: PaginatedGetPostingFBOListFilter,
) -> GetPostingFBOListResponseResultWrapper:
    return request_api.request_api_json(
        "POST",
        "/v2/posting/fbo/list",
        credentials,
        data,
        response_cls=GetPostingFBOListResponseResultWrapper,
    )


def get_posting_fbo_list_iterative(
    credentials: credentials.Credentials,
    data: PaginatedGetPostingFBOListFilter,
) -> Iterator[GetPostingFBOListResponseResult]:
    return make_iterative.make_iterative_via_offset(
        request=data,
        requester=lambda: get_posting_fbo_list(credentials, data),
        extract_response_items=lambda response: response.result,
    )
