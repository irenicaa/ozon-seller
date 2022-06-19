from dataclasses import dataclass, field
from typing import Optional, Generator
import datetime

from dataclasses_json import dataclass_json

import request_api
import credentials

# Request

@dataclass_json
@dataclass
class OderData:
    posting_number: Optional[str]
    product_id: Optional[int]
    country_iso_code: Optional[str]

# Response
# TODO: example
@dataclass_json
@dataclass
class GetCountrySetFBSResponseResult:
    product_id: int
    is_gtd_needed: bool

def posting_fbs_product_country_set(
    credentials: credentials.Credentials,
    data: OderData,
) -> GetCountrySetFBSResponseResult:
    response = request_api.request_api_raw(
        'POST',
        '/v2/posting/fbs/product/country/set',
        credentials,
        data.to_json(),
    )
    return GetCountrySetFBSResponseResult.schema().loads(response)
