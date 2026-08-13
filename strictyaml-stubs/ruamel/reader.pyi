from collections.abc import Callable
from typing import (
    Any,
    ClassVar,
    TextIO,
)

from .error import (
    FileMark,
    StringMark,
    YAMLError,
)
from .util import LazyEval

from .._types import StreamType  # isort: skip

__all__ = ("ReaderError", "Reader")

class ReaderError(YAMLError):
    name: str
    character: str | bytes
    position: int
    encoding: str
    reason: str

    def __init__(
        self,
        name: str,
        position: int,
        character: str | bytes,
        encoding: str,
        reason: str,
    ) -> None: ...

class Reader:
    NON_PRINTABLE: ClassVar[LazyEval]
    _printable_ascii: ClassVar[bytes]

    buffer: str
    column: int
    encoding: str | None
    eof: bool
    index: int
    line: int
    loader: Any | None
    name: str | None
    pointer: int
    raw_buffer: Any | None
    raw_decode: Callable[[bytes, str, bool], tuple[str, int]] | None
    _stream: StreamType | None
    stream_pointer: int

    def __init__(self, stream: StreamType, loader: Any | None = None) -> None: ...
    def reset_reader(self) -> None: ...
    @property
    def stream(self) -> Any: ...
    # Any -- object with attribute, read
    @stream.setter
    def stream(self, val: str | bytes | Any | None) -> None: ...
    def peek(self, index: int = 0) -> TextIO: ...
    def prefix(self, length: int = 1) -> Any: ...
    def forward_1_1(self, length: int = 1) -> None: ...
    def forward(self, length: int = 1) -> None: ...
    def get_mark(self) -> StringMark | FileMark: ...
    def determine_encoding(self) -> None: ...
    @classmethod
    def _get_non_printable_ascii(cls, data: bytes) -> tuple[int, str] | None: ...
    @classmethod
    def _get_non_printable_regex(cls, data: str) -> tuple[int, str] | None: ...
    @classmethod
    def _get_non_printable(cls, data: bytes | str) -> tuple[int, str] | None: ...
    def check_printable(self, data: Any) -> None: ...
    def update(self, length: int) -> None: ...
    def update_raw(self, size: int | None = None) -> None: ...
