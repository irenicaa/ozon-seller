from dataclasses import dataclass


CLIENT_ID_HEADER_KEY = "Client-Id"
API_KEY_HEADER_KEY = "Api-Key"


@dataclass
class Credentials:
    client_id: str
    api_key: str

    def to_headers(self) -> dict[str, str]:
        return {
            CLIENT_ID_HEADER_KEY: self.client_id,
            API_KEY_HEADER_KEY: self.api_key,
        }
