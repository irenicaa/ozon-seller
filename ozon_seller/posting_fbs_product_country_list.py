from dataclasses import dataclass
from typing import Optional

from .common import credentials, request_api
from .common.data_class_json_mixin import DataClassJsonMixin


# Request


@dataclass
class CountryFilter(DataClassJsonMixin):
    name_search: Optional[str] = None


# Response


@dataclass
class GetPostingFBSProductCountryListResponseResult(DataClassJsonMixin):
    name: str
    country_iso_code: str


@dataclass
class GetPostingFBSProductCountryListResponseResultWrapper(DataClassJsonMixin):
    result: list[GetPostingFBSProductCountryListResponseResult]


def get_posting_fbs_product_country_list(
    credentials: credentials.Credentials,
    data: CountryFilter,
) -> GetPostingFBSProductCountryListResponseResultWrapper:
    return request_api.request_api_json(
        "POST",
        "/v2/posting/fbs/product/country/list",
        credentials,
        data,
        response_cls=GetPostingFBSProductCountryListResponseResultWrapper,
    )
