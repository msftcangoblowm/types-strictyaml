import builtins
from typing import (
    Any,
    Final,
)

from strictyaml.representation import YAML
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

unicode: Final[type[builtins.str]]

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
    __slots__ = (
        "_key_validator",
        "_value_validator",
        "_maximum_keys",
        "_minimum_keys",
    )
    # Accepts ANY ScalarValidator (Str, Float, Int, Bool, Datetime, etc.)
    _key_validator: ScalarValidator
    _value_validator: Validator
    _maximum_keys: int | None
    _minimum_keys: int | None
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
    # Data keys match the validated type (could be str, float, int, ...)
    def to_yaml(self, data: dict[Any, Any]) -> CommentedMap: ...

class Map(MapValidator):
    __slots__ = (
        "_validator",
        "_key_validator",
        "_validator_dict",
        "_required_keys",
        "_defaults",
    )
    _validator: MapValidatorType

    # MUST be ScalarValidator to support custom validators (e.g., Slug, XPathValidator)
    # Warning: Non-string scalars (Float, Int) are technically allowed but unsafe
    # due to hash precision and Optional wrapper assumptions.
    _key_validator: ScalarValidator

    # Normalized keys (str or validated scalar result) -> Validator
    _validator_dict: dict[str, Validator]

    # List of required key names (str)
    _required_keys: list[str]
    #    Key -> Default Value
    _defaults: dict[str, Any]

    def __init__(
        self,
        validator: MapValidatorType,
        key_validator: ScalarValidator | None = None,
    ) -> None: ...
    @property
    def key_validator(self) -> ScalarValidator: ...
    def get_validator(self, key: str) -> Validator: ...
    def unexpected_key(
        self,
        # calls key.expecting_but_found
        key: YAMLChunk,
        # calls YAML.scalar
        yaml_key: YAML,
        # unused
        value: Any,
        # unused
        chunk: YAMLChunk,
    ) -> None: ...
    def validate(self, chunk: YAMLChunk) -> None: ...
    def to_yaml(
        self,
        data: dict[str, Any],
    ) -> CommentedMap: ...

class MapCombined(Map):
    __slots__ = ("_value_validator",)
    _value_validator: Validator

    def __init__(
        self,
        map_validator: MapValidatorType,
        # see Map commentary
        key_validator: ScalarValidator,
        value_validator: Validator,
    ) -> None: ...
    def get_validator(self, key: str) -> Validator: ...
    def unexpected_key(
        self,
        key: YAMLChunk,
        yaml_key: YAML,
        value: Any,
        chunk: YAMLChunk,
    ) -> None: ...

class Seq(SeqValidator):
    __slots__ = ("_validator",)
    _validator: Validator

    def __init__(self, validator: Validator) -> None: ...
    def validate(self, chunk: YAMLChunk) -> None: ...
    def to_yaml(self, data: list[Any]) -> CommentedSeq: ...

class FixedSeq(SeqValidator):
    __slots__ = ("_validator",)
    _validators: list[Validator]

    def __init__(self, validators: list[Validator]) -> None: ...
    def validate(self, chunk: YAMLChunk) -> None: ...
    def to_yaml(self, data: list[Any]) -> CommentedSeq: ...

class UniqueSeq(SeqValidator):
    __slots__ = ("_validator",)
    _validator: ScalarValidator

    def __init__(self, validator: ScalarValidator) -> None: ...
    def validate(self, chunk: YAMLChunk) -> None: ...
    def to_yaml(self, data: list[Any]) -> CommentedSeq: ...
