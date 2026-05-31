from typing import Any as _Any

from strictyaml.compound import (
    FixedSeq,
    Map,
)
from strictyaml.scalar import (
    Bool,
    EmptyDict,
    EmptyList,
    Float,
    Int,
    ScalarValidator,
    Str,
)
from strictyaml.validators import Validator
from strictyaml.yamllocation import YAMLChunk
from typing_extensions import TypeAlias

FromDocument: TypeAlias = FixedSeq | Map | Str
FromData: TypeAlias = FixedSeq | Map | EmptyDict | EmptyList | Bool | Float | Int | Str

__all__ = ("Any",)

def schema_from_document(document: _Any) -> FromDocument: ...
def schema_from_data(
    data: _Any,
    allow_empty: bool,
) -> FromData: ...

class Any(Validator):
    def validate(self, chunk: YAMLChunk) -> FromDocument: ...
    def to_yaml(self, data: _Any, allow_empty: bool | None = False) -> FromData: ...
    @property
    def key_validator(self) -> ScalarValidator: ...
