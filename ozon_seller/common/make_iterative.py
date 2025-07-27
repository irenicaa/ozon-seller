from typing import TypeVar, Callable, Iterator


T = TypeVar("T")


def make_iterative(
    requester: Callable[[], T],
    get_response_length: Callable[[T], int],
    shift_request: Callable[[T], None],
) -> Iterator[T]:
    while True:
        response = requester()
        if get_response_length(response) == 0:
            break

        yield response

        shift_request(response)
