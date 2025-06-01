from dataclasses import dataclass

from .common import credentials, request_api
from .common.data_class_json_mixin import DataClassJsonMixin


# Request


@dataclass
class FBSPackageData(DataClassJsonMixin):
    posting_number: list[str]


def get_posting_fbs_package_label(
    credentials: credentials.Credentials,
    data: FBSPackageData,
) -> bytes:
    response = request_api.request_api_raw(
        "POST",
        "/v2/posting/fbs/package-label",
        credentials,
        data.to_json(),
    )
    return response.content
