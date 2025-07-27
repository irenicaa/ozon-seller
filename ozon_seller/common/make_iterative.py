from typing import TypeVar, Callable, Iterator


T = TypeVar("T")
I = TypeVar("I")
U = TypeVar("U")


def make_iterative(
    requester: Callable[[], T],
    extract_response_items: Callable[[T], list[I]],
    shift_request: Callable[[T], None],
) -> Iterator[I]:
    while True:
        response = requester()

        response_items = extract_response_items(response)
        if len(response_items) == 0:
            break

        yield from response_items

        shift_request(response)


def make_iterative_via_offset(
    request: U,
    requester: Callable[[], T],
    extract_response_items: Callable[[T], list[I]],
    offset_attribute_name: str = "offset",
) -> Iterator[I]:
    def _shift_request(response: T) -> None:
        nonlocal request

        previous_offset = getattr(request, offset_attribute_name)
        if previous_offset is None:
            previous_offset = 0

        next_offset = previous_offset + len(extract_response_items(response))
        setattr(request, offset_attribute_name, next_offset)

    return make_iterative(
        requester=requester,
        extract_response_items=extract_response_items,
        shift_request=_shift_request,
    )


def make_iterative_via_cursor(
    request: U,
    requester: Callable[[], T],
    extract_response_items: Callable[[T], list[I]],
    cursor_attribute_name: str = "cursor",
) -> Iterator[I]:
    def _shift_request(response: T) -> None:
        nonlocal request

        next_cursor = getattr(response, cursor_attribute_name)
        setattr(request, cursor_attribute_name, next_cursor)

    return make_iterative(
        requester=requester,
        extract_response_items=extract_response_items,
        shift_request=_shift_request,
    )
