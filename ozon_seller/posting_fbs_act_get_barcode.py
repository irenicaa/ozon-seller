from dataclasses import dataclass

from .common import credentials, request_api
from .common.data_class_json_mixin import DataClassJsonMixin


# Request


@dataclass
class FBSActData(DataClassJsonMixin):
    id: int


def get_posting_fbs_act_barcode(
    credentials: credentials.Credentials,
    data: FBSActData,
) -> bytes:
    response = request_api.request_api_raw(
        "POST",
        "/v2/posting/fbs/act/get-barcode",
        credentials,
        data.to_json(),
    )
    return response.content
