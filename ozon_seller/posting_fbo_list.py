import datetime
from dataclasses import dataclass, field
from typing import Generator, Optional

from dataclasses_json import CatchAll, Undefined, config, dataclass_json
from marshmallow import fields

from . import returns_fbs
from .common import credentials, request_api


def parse_datetime(value):
    if value is None:
        return None
    elif isinstance(value, str):
        return datetime.datetime.fromisoformat(value)
    elif isinstance(value, datetime.datetime):
        return value
    else:
        raise RuntimeError("unsopported time for a datetime field")


# Request


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class PostingAdditionalFields:
    analytics_data: Optional[bool] = False
    financial_data: Optional[bool] = False


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetPostingFBOListFilter:
    since: Optional[datetime.datetime] = field(
        metadata=config(encoder=returns_fbs.format_datetime),
        default=None,
    )
    to: Optional[datetime.datetime] = field(
        metadata=config(encoder=returns_fbs.format_datetime),
        default=None,
    )
    status: Optional[str] = None


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class PaginatedGetPostingFBOListFilter:
    filter: Optional[GetPostingFBOListFilter] = None
    dir: Optional[str] = "ASC"
    translit: Optional[bool] = False
    limit: Optional[int] = None
    offset: Optional[int] = None
    with_: Optional[PostingAdditionalFields] = field(
        default=None,
        metadata=config(field_name="with"),
    )


# Response


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetPostingFBOListResponseProduct:
    digital_code: str
    name: str
    offer_id: str
    price: str
    quantity: int
    sku: int


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetPostingFBOListResponsePicking:
    amount: float
    moment: datetime.datetime = field(
        metadata=config(
            decoder=datetime.datetime.fromisoformat,
            mm_field=fields.DateTime(format="iso"),
        ),
    )
    tag: str


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetPostingFBOListResponseFinancialDataServices:
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


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetPostingFBOListResponseFinancialDataProduct:
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


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetPostingFBOListResponseFinancialData:
    posting_services: GetPostingFBOListResponseFinancialDataServices
    products: list[GetPostingFBOListResponseFinancialDataProduct]


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetPostingFBOListResponseAnalyticsData:
    city: str
    delivery_type: str
    is_legal: bool
    is_premium: bool
    payment_type_group_name: str
    region: str
    warehouse_id: int
    warehouse_name: str


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetPostingFBOAdditionalDataItem:
    key: str
    value: str


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetPostingFBOListResponseResult:
    additional_data: list[GetPostingFBOAdditionalDataItem]
    analytics_data: Optional[GetPostingFBOListResponseAnalyticsData]
    cancel_reason_id: int
    created_at: Optional[datetime.datetime] = field(
        metadata=config(
            decoder=parse_datetime,
            mm_field=fields.DateTime(format="iso", allow_none=True),
        ),
    )
    financial_data: Optional[GetPostingFBOListResponseFinancialData]
    in_process_at: Optional[datetime.datetime] = field(
        metadata=config(
            decoder=parse_datetime,
            mm_field=fields.DateTime(format="iso", allow_none=True),
        ),
    )
    order_id: int
    order_number: str
    posting_number: str
    products: list[GetPostingFBOListResponseProduct]
    status: str


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetPostingFBOListResponseResultWrapper:
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
) -> Generator[GetPostingFBOListResponseResultWrapper, None, None]:
    while True:
        list = get_posting_fbo_list(credentials, data)
        if list.result == []:
            break

        yield list

        data.offset += data.limit
