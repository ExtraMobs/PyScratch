from typing import Any

_global = {}


def set(name: Any, data: Any) -> None:
    _global[name] = data


def get(name: Any) -> Any:
    return _global[name]
