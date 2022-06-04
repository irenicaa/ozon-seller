from dataclasses import dataclass, field
from typing import Optional, Generator
import datetime

from dataclasses_json import dataclass_json, Undefined, config, CatchAll
from marshmallow import fields

import request_api
import credentials
import returns_fbs

# Request

@dataclass_json
@dataclass
class CountryFilter:
    name_search: Optional[str] = None

# Response

@dataclass_json
@dataclass
class GetFBSProductCountryListResponseResult:
    name: str
    country_iso_code: str

@dataclass_json
@dataclass
class GetFBSProductCountryListResponseResultWrapper:
    result: list[GetFBSProductCountryListResponseResult]

def get_fbs_product_country_list(
    credentials: credentials.Credentials,
    data: CountryFilter,
) -> GetFBSProductCountryListResponseResultWrapper:
    response = request_api.request_api_raw(
        'POST',
        '/v2/posting/fbs/product/country/list',
        credentials,
        data.to_json(),
    )
    return GetFBSProductCountryListResponseResultWrapper.schema().loads(response)
