import datetime
from dataclasses import dataclass, field
from typing import Generator, Optional

from dataclasses_json import (
    CatchAll,
    Undefined,
    config,
    dataclass_json,
    DataClassJsonMixin,
)
from marshmallow import fields

from .common import credentials, request_api

# Request


@dataclass
class CountryFilter(DataClassJsonMixin):
    name_search: Optional[str] = None


# Response


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetPostingFBSProductCountryListResponseResult:
    name: str
    country_iso_code: str


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetPostingFBSProductCountryListResponseResultWrapper:
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
