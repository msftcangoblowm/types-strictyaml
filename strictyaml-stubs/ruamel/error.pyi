from typing import Any

__all__ = [
    "FileMark",
    "StringMark",
    "CommentMark",
    "YAMLError",
    "MarkedYAMLError",
    "ReusedAnchorWarning",
    "UnsafeLoaderWarning",
    "MarkedYAMLWarning",
    "MarkedYAMLFutureWarning",
]

class StreamMark:
    __slots__ = ("name", "index", "line", "column")

    def __init__(self, name: Any, index: int, line: int, column: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

class FileMark(StreamMark):
    __slots__ = ()

class StringMark(StreamMark):
    __slots__ = ("name", "index", "line", "column", "buffer", "pointer")

    def __init__(
        self,
        name: Any,
        index: int,
        line: int,
        column: int,
        buffer: Any,
        pointer: Any,
    ) -> None: ...
    def get_snippet(self, indent: int = 4, max_length: int = 75) -> Any: ...

class CommentMark:
    __slots__ = ("column",)

    def __init__(self, column: Any) -> None: ...

class YAMLError(Exception): ...

class MarkedYAMLError(YAMLError):
    def __init__(
        self,
        context: Any | None = None,
        context_mark: Any | None = None,
        problem: Any | None = None,
        problem_mark: Any | None = None,
        note: Any | None = None,
        warn: Any | None = None,
    ) -> None: ...

class YAMLStreamError(Exception): ...
class YAMLWarning(Warning): ...

class MarkedYAMLWarning(YAMLWarning):
    def __init__(
        self,
        context: Any | None = None,
        context_mark: Any | None = None,
        problem: Any | None = None,
        problem_mark: Any | None = None,
        note: Any | None = None,
        warn: Any | None = None,
    ) -> None: ...

class ReusedAnchorWarning(YAMLWarning): ...

class UnsafeLoaderWarning(YAMLWarning):
    text: str

class MantissaNoDotYAML1_1Warning(YAMLWarning):
    def __init__(self, node: Any, flt_str: Any) -> None: ...

class YAMLFutureWarning(Warning): ...

class MarkedYAMLFutureWarning(YAMLFutureWarning):
    def __init__(
        self,
        context: Any | None = None,
        context_mark: Any | None = None,
        problem: Any | None = None,
        problem_mark: Any | None = None,
        note: Any | None = None,
        warn: Any | None = None,
    ) -> None: ...
