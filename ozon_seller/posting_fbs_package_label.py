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
    return request_api.request_api_content(
        "POST",
        "/v2/posting/fbs/package-label",
        credentials,
        data,
    )
