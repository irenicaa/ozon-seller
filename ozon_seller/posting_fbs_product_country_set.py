import datetime
from dataclasses import dataclass, field
from typing import Generator, Optional

from dataclasses_json import Undefined, dataclass_json, DataClassJsonMixin

from .common import credentials, request_api

# Request


@dataclass
class OderData(DataClassJsonMixin):
    posting_number: Optional[str]
    product_id: Optional[int]
    country_iso_code: Optional[str]


# Response
# TODO: example
@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetCountrySetFBSResponseResult:
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
