from typing import (
    Any,
    ClassVar,
    SupportsIndex,
)

from typing_extensions import Self

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
    __slots__ = (Anchor.attrib,)

    def __new__(cls, *args: Any, **kw: Any) -> Any: ...
    def replace(
        self,
        old: Self | str,
        new: Self | str,
        maxreplace: SupportsIndex = -1,
    ) -> Self: ...
    @property
    def anchor(self) -> Anchor: ...
    # any is a Python fcn name. Rename param "any" --> "any_"
    def yaml_anchor(self, any: bool = False) -> Anchor | None: ...
    def yaml_set_anchor(self, value: Any, always_dump: bool = False) -> None: ...

class LiteralScalarString(ScalarString):
    __slots__ = ("comment",)
    style: ClassVar[str]
    # unused; typing irrelevant
    comment: Any

    def __new__(cls, value: str, anchor: Any | None = None) -> Any: ...

PreservedScalarString = LiteralScalarString

class FoldedScalarString(ScalarString):
    __slots__ = ("fold_pos", "comment")
    style: ClassVar[str]
    # unused
    fold_pos: Any
    # unused
    comment: Any

    def __new__(cls, value: str, anchor: Any | None = None) -> Self: ...

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
