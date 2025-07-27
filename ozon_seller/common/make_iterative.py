from typing import TypeVar, Callable, Iterator


T = TypeVar("T")
U = TypeVar("U")


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


def make_iterative_via_offset(
    request: U,
    requester: Callable[[], T],
    get_response_length: Callable[[T], int],
    offset_attribute_name: str = "offset",
) -> Iterator[T]:
    def _shift_request(response: T) -> None:
        nonlocal request

        previous_offset = getattr(request, offset_attribute_name)
        if previous_offset is None:
            previous_offset = 0

        next_offset = previous_offset + get_response_length(response)
        setattr(request, offset_attribute_name, next_offset)

    return make_iterative(
        requester=requester,
        get_response_length=get_response_length,
        shift_request=_shift_request,
    )
