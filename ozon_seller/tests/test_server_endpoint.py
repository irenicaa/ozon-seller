from dataclasses import dataclass
from typing import Optional

from ..common import credentials


@dataclass
class TestServerEndpoint:
    expected_method: str
    expected_endpoint: str
    expected_credentials: credentials.Credentials
    expected_request_json: Optional[str]
    provided_response_type: str
    provided_response_data: str
