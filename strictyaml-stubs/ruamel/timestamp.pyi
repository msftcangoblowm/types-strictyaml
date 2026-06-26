import datetime
from typing import (
    Any,
    SupportsIndex,
)

from typing_extensions import Self

__all__ = ("TimeStamp",)

class TimeStamp(datetime.datetime):
    def __init__(self, *args: Any, **kw: Any) -> None: ...
    def __new__(cls, *args: Any, **kw: Any) -> Any: ...
    def __deepcopy__(self, memo: Any) -> Any: ...
    def replace(  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        year: SupportsIndex | None = ...,
        month: SupportsIndex | None = ...,
        day: SupportsIndex | None = ...,
        hour: SupportsIndex | None = ...,
        minute: SupportsIndex | None = ...,
        second: SupportsIndex | None = ...,
        microsecond: SupportsIndex | None = ...,
        tzinfo: datetime.tzinfo | bool | None = ...,
        fold: SupportsIndex | None = ...,
    ) -> Self: ...
    # py310 rtype is datetime.datetime py311+ rtype is Self
