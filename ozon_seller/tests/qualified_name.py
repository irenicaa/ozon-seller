from typing import Union


def get_full_qualified_name(obj: object) -> str:
    return f"{get_last_module(obj)}.{get_qualified_name(obj)}"


def get_last_module(obj: Union[object, type[object]]) -> str:
    return _get_class(obj).__module__.split(".")[-1]


def get_qualified_name(obj: Union[object, type[object]]) -> str:
    return _get_class(obj).__qualname__


def _get_class(obj: Union[object, type[object]]) -> type[object]:
    return obj if callable(obj) or isinstance(obj, type) else obj.__class__
