from typing import Any

from typing_extensions import (
    Self,
    TypeAlias,
)

__all__ = [
    "BinaryInt",
    "DecimalInt",
    "HexInt",
    "HexCapsInt",
    "OctalInt",
    "ScalarInt",
]

NoLimitInt: TypeAlias = int

class ScalarInt(NoLimitInt):
    def __new__(cls, *args: Any, **kw: Any) -> Any: ...
    def __iadd__(self, a: Any) -> Self: ...  # type: ignore
    def __ifloordiv__(self, a: Any) -> Self: ...  # type: ignore
    def __imul__(self, a: Any) -> Self: ...  # type: ignore
    def __ipow__(self, a: Any) -> Self: ...  # type: ignore
    def __isub__(self, a: Any) -> Self: ...  # type: ignore
    @property
    def anchor(self) -> Any: ...
    def yaml_anchor(self, any: bool = False) -> Any: ...
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
