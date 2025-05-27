TEST_DATA_DIRECTORY = "test-data"


def get_full_qualified_name(obj: object) -> str:
    return f"{get_last_module(obj)}.{get_qualified_name(obj)}"


def get_last_module(obj: object) -> str:
    return obj.__module__.split(".")[-1]


def get_qualified_name(obj: object) -> str:
    return obj.__class__.__qualname__
