from typing import Any

from typing_extensions import (
    Self,
    disjoint_base,
)

from .anchor import Anchor

__all__ = [
    "BinaryInt",
    "DecimalInt",
    "HexInt",
    "HexCapsInt",
    "OctalInt",
    "ScalarInt",
]

# NoLimitInt: TypeAlias = int

# replaced NoLimitInt --> int. py2 compat unneeded
@disjoint_base
class ScalarInt(int):
    _width: Any | None
    _underscore: str | None

    def __new__(cls, *args: Any, **kw: Any) -> Self: ...
    def __iadd__(self, a: Any) -> Self: ...  # type: ignore
    def __ifloordiv__(self, a: Any) -> Self: ...  # type: ignore
    def __imul__(self, a: Any) -> Self: ...  # type: ignore
    def __ipow__(self, a: Any) -> Self: ...  # type: ignore
    def __isub__(self, a: Any) -> Self: ...  # type: ignore
    @property
    def anchor(self) -> Anchor: ...
    def yaml_anchor(self, any: bool = False) -> Anchor | None: ...
    def yaml_set_anchor(self, value: Any, always_dump: bool = False) -> None: ...

class BinaryInt(ScalarInt):
    def __new__(
        cls,
        value: Any,
        width: Any | None = None,
        underscore: Any | None = None,
        anchor: Any | None = None,
    ) -> Any: ...

class OctalInt(ScalarInt):
    def __new__(
        cls,
        value: Any,
        width: Any | None = None,
        underscore: Any | None = None,
        anchor: Any | None = None,
    ) -> Any: ...

class HexInt(ScalarInt):
    def __new__(
        cls,
        value: Any,
        width: Any | None = None,
        underscore: Any | None = None,
        anchor: Any | None = None,
    ) -> Any: ...

class HexCapsInt(ScalarInt):
    def __new__(
        cls,
        value: Any,
        width: Any | None = None,
        underscore: Any | None = None,
        anchor: Any | None = None,
    ) -> Any: ...

class DecimalInt(ScalarInt):
    def __new__(
        cls,
        value: Any,
        width: Any | None = None,
        underscore: Any | None = None,
        anchor: Any | None = None,
    ) -> Any: ...
