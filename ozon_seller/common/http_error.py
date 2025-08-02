from typing import Generic, TypeVar


T = TypeVar("T")


class HTTPError(RuntimeError, Generic[T]):
    def __init__(
        self,
        message: str,
        status: int,
        response_data: T,
        *args: object,
    ) -> None:
        super().__init__(message, status, response_data, *args)

        self.message = message
        self.status = status
        self.response_data = response_data

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, HTTPError):
            return NotImplemented

        return (
            self.message == other.message
            and self.status == other.status
            and self.response_data == other.response_data
        )
