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
    name: Any
    index: int
    line: int
    column: int

    def __init__(self, name: Any, index: int, line: int, column: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

class FileMark(StreamMark):
    __slots__ = ()

class StringMark(StreamMark):
    # __slots__ inheritance misconception. Source code needs fix. Stubs shows correction.
    __slots__ = ("buffer", "pointer")

    buffer: Any
    pointer: Any

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
    column: Any

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
    # source code lacks __slots__
    context: Any | None
    context_mark: Any | None
    problem: Any | None
    problem_mark: Any | None
    note: Any | None
    warn: Any | None

    # Source code lacks ``super().__init__()`` call
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
    # source code lacks __slots__
    node: Any
    flt: Any

    # Source code lacks ``super().__init__()`` call
    def __init__(self, node: Any, flt_str: Any) -> None: ...

class YAMLFutureWarning(Warning): ...

class MarkedYAMLFutureWarning(YAMLFutureWarning):
    context: Any | None
    context_mark: Any | None
    problem: Any | None
    problem_mark: Any | None
    note: Any | None
    warn: Any | None

    # Source code lacks ``super().__init__()`` call
    def __init__(
        self,
        context: Any | None = None,
        context_mark: Any | None = None,
        problem: Any | None = None,
        problem_mark: Any | None = None,
        note: Any | None = None,
        warn: Any | None = None,
    ) -> None: ...
