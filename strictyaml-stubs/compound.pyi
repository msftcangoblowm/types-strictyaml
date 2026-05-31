from typing import Any

from strictyaml.ruamel.comments import (
    CommentedMap,
    CommentedSeq,
)
from strictyaml.scalar import ScalarValidator
from strictyaml.validators import (
    MapValidator,
    SeqValidator,
    Validator,
)
from strictyaml.yamllocation import YAMLChunk
from typing_extensions import TypeAlias

__all__ = (
    "Map",
    "MapCombined",
    "MapPattern",
    "Optional",
    "Seq",
    "FixedSeq",
    "UniqueSeq",
)

class Optional:
    __slots__ = ("key", "default", "drop_if_none")
    key: str
    default: Any | None
    drop_if_none: bool | None

    def __init__(
        self,
        key: str,
        default: Any | None = None,
        drop_if_none: bool | None = True,
    ) -> None: ...

MapValidatorType: TypeAlias = dict[str | Optional, Validator]

class MapPattern(MapValidator):
    def __init__(
        self,
        key_validator: ScalarValidator,
        value_validator: Validator,
        minimum_keys: int | None = None,
        maximum_keys: int | None = None,
    ) -> None: ...
    @property
    def key_validator(self) -> ScalarValidator: ...
    def validate(self, chunk: YAMLChunk) -> None: ...
    def to_yaml(self, data: dict[Any, Any]) -> CommentedMap: ...

class Map(MapValidator):
    def __init__(
        self,
        validator: MapValidatorType,
        key_validator: ScalarValidator | None = None,
    ) -> None: ...
    @property
    def key_validator(self) -> ScalarValidator: ...
    def get_validator(self, key: ScalarValidator) -> Validator: ...
    def unexpected_key(
        self,
        key: Any,
        yaml_key: ScalarValidator,
        value: Validator,
        chunk: YAMLChunk,
    ) -> None: ...
    def validate(self, chunk: YAMLChunk) -> None: ...
    def to_yaml(
        self,
        data: dict[ScalarValidator, Validator],
    ) -> CommentedMap: ...

class MapCombined(Map):
    def __init__(
        self,
        map_validator: MapValidatorType,
        key_validator: ScalarValidator,
        value_validator: Validator,
    ) -> None: ...
    def get_validator(self, key: ScalarValidator) -> Validator: ...
    def unexpected_key(
        self,
        key: Any,
        yaml_key: ScalarValidator,
        value: Validator,
        chunk: YAMLChunk,
    ) -> None: ...

class Seq(SeqValidator):
    __slots__ = ("_validator",)
    _validator: Validator

    def __init__(self, validator: Validator) -> None: ...
    def validate(self, chunk: YAMLChunk) -> None: ...
    def to_yaml(self, data: list[Any]) -> CommentedSeq: ...

class FixedSeq(SeqValidator):
    def __init__(self, validators: list[Validator]) -> None: ...
    def validate(self, chunk: YAMLChunk) -> None: ...
    def to_yaml(self, data: list[Any]) -> CommentedSeq: ...

class UniqueSeq(SeqValidator):
    def __init__(self, validator: Validator) -> None: ...
    def validate(self, chunk: YAMLChunk) -> None: ...
    def to_yaml(self, data: list[Any]) -> CommentedSeq: ...
