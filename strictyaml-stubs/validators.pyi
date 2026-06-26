import builtins
from typing import (
    Any,
    Final,
)

from strictyaml.representation import YAML
from strictyaml.yamllocation import YAMLChunk

__all__ = (
    "MapValidator",
    "OrValidator",
    "SeqValidator",
    "Validator",
)

unicode: Final[type[builtins.str]]

class Validator:
    def __or__(self, other: Any) -> "OrValidator": ...  # noqa: Y020
    def __call__(self, chunk: YAMLChunk) -> YAML: ...

class OrValidator(Validator):
    def __init__(self, validator_a: Validator, validator_b: Validator) -> None: ...
    def to_yaml(self, value: Any) -> str: ...
    def __call__(self, chunk: YAMLChunk) -> YAML: ...

class MapValidator(Validator):
    def _should_be_mapping(self, data: dict[Any, Any]) -> None: ...

class SeqValidator(Validator):
    def _should_be_list(self, data: list[Any]) -> None: ...
