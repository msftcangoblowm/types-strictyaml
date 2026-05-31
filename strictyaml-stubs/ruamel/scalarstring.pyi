from typing import (
    Any,
    ClassVar,
    SupportsIndex,
)

from .anchor import Anchor

__all__ = [
    "DoubleQuotedScalarString",
    "FoldedScalarString",
    "LiteralScalarString",
    "PlainScalarString",
    "PreservedScalarString",
    "ScalarString",
    "SingleQuotedScalarString",
]

class ScalarString(str):
    __slots__ = Anchor.attrib

    def __new__(cls, *args: Any, **kw: Any) -> Any: ...
    def replace(self, old: Any, new: Any, maxreplace: SupportsIndex = -1) -> Any: ...
    @property
    def anchor(self) -> Any: ...
    def yaml_anchor(self, any: bool = False) -> Any: ...
    def yaml_set_anchor(self, value: Any, always_dump: bool = False) -> None: ...

class LiteralScalarString(ScalarString):
    __slots__ = ("comment",)
    style: ClassVar[str]

    def __new__(cls, value: str, anchor: Any | None = None) -> Any: ...

PreservedScalarString = LiteralScalarString

class FoldedScalarString(ScalarString):
    __slots__ = ("fold_pos", "comment")
    style: ClassVar[str]

    def __new__(cls, value: str, anchor: Any | None = None) -> Any: ...

class SingleQuotedScalarString(ScalarString):
    __slots__ = ()

    style: ClassVar[str]

    def __new__(cls, value: str, anchor: Any | None = None) -> Any: ...

class DoubleQuotedScalarString(ScalarString):
    __slots__ = ()

    style: ClassVar[str]

    def __new__(cls, value: str, anchor: Any | None = None) -> Any: ...

class PlainScalarString(ScalarString):
    __slots__ = ()

    style: ClassVar[str]

    def __new__(cls, value: str, anchor: Any | None = None) -> Any: ...

def preserve_literal(s: str) -> str: ...
def walk_tree(base: Any, map: Any | None = None) -> None: ...
