from dataclasses import dataclass
from typing import Optional

from .common import credentials, request_api
from .common.data_class_json_mixin import DataClassJsonMixin


# Request


@dataclass
class OderData(DataClassJsonMixin):
    posting_number: Optional[str]
    product_id: Optional[int]
    country_iso_code: Optional[str]


# Response


@dataclass
class GetCountrySetFBSResponseResult(DataClassJsonMixin):
    product_id: int
    is_gtd_needed: bool


def posting_fbs_product_country_set(
    credentials: credentials.Credentials,
    data: OderData,
) -> GetCountrySetFBSResponseResult:
    return request_api.request_api_json(
        "POST",
        "/v2/posting/fbs/product/country/set",
        credentials,
        data,
        response_cls=GetCountrySetFBSResponseResult,
    )
