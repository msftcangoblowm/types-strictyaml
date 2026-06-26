import builtins
import decimal
from typing import (
    Any,
    Final,
)

import strictyaml as s
from strictyaml.ruamel.comments import (
    CommentedMap,
    CommentedSeq,
)

unicode: Final[type[builtins.str]]

__all__ = (
    "comma_separated_positions",
    "flatten",
    "has_number_type",
    "is_decimal",
    "is_hexadecimal",
    "is_infinity",
    "is_integer",
    "is_not_a_number",
    "is_string",
    "ruamel_structure",
)

def flatten(items: list[Any]) -> list[Any]: ...
def has_number_type(value: float | decimal.Decimal) -> bool: ...
def is_string(value: Any) -> bool: ...
def is_integer(value: str) -> bool: ...
def is_hexadecimal(value: str) -> bool: ...
def is_decimal(value: str) -> bool: ...
def is_infinity(value: str) -> bool: ...
def is_not_a_number(value: str) -> bool: ...
def comma_separated_positions(text: str) -> list[tuple[int, int]]: ...
def ruamel_structure(
    data: dict[Any, Any] | list[Any] | bool | float | str,
    validator: s.Validator | None = None,
) -> CommentedMap | CommentedSeq | str | Any: ...
