from typing import Any

from typing_extensions import (
    Self,
    disjoint_base,
)

from .anchor import Anchor

__all__ = ("ScalarBoolean",)

@disjoint_base
class ScalarBoolean(int):
    def __new__(cls, *args: Any, **kw: Any) -> Self: ...
    @property
    def anchor(self) -> Anchor: ...
    # any is a Python built-in fcn. rename any --> any_
    def yaml_anchor(self, any: bool = False) -> Anchor | None: ...
    # Will not work. Lacks ScalarBoolean.anchor setter or attribute
    def yaml_set_anchor(self, value: Any, always_dump: bool = False) -> None: ...
