from typing import Generic, TypeVar

T = TypeVar("T")


class HTTPError(RuntimeError, Generic[T]):
    def __init__(
        self,
        message: str,
        status: int,
        response_data: T,
        *args,
    ):
        super().__init__(message, status, response_data, *args)

        self.message = message
        self.status = status
        self.response_data = response_data
