from dataclasses import dataclass


@dataclass
class Credentials:
    client_id: str
    api_key: str

    def to_headers(self) -> dict[str, str]:
        return {
            "Client-Id": self.client_id,
            "Api-Key": self.api_key,
        }
