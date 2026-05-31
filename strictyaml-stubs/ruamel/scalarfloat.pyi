from typing import Any

from typing_extensions import Self

__all__ = (
    "ExponentialFloat",
    "ExponentialCapsFloat",
    "ScalarFloat",
)

class ScalarFloat(float):
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
    def dump(self, out: Any = ...) -> Any: ...

class ExponentialFloat(ScalarFloat):
    def __new__(
        cls,
        value: Any,
        width: Any | None = None,
        underscore: Any | None = None,
    ) -> Any: ...

class ExponentialCapsFloat(ScalarFloat):
    def __new__(
        cls,
        value: Any,
        width: Any | None = None,
        underscore: Any | None = None,
    ) -> Any: ...
