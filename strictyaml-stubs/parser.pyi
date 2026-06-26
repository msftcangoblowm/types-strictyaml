from typing import (
    Any,
    ClassVar,
)

from strictyaml.representation import YAML
from strictyaml.ruamel.compat import VersionType
from strictyaml.ruamel.composer import Composer
from strictyaml.ruamel.constructor import RoundTripConstructor
from strictyaml.ruamel.parser import RoundTripParser
from strictyaml.ruamel.reader import Reader
from strictyaml.ruamel.resolver import VersionedResolver
from strictyaml.ruamel.scanner import RoundTripScanner
from strictyaml.validators import Validator

__all__ = (
    "StrictYAMLConstructor",
    "StrictYAMLScanner",
    "StrictYAMLLoader",
    "as_document",
    "dirty_load",
    "load",
)

class StrictYAMLConstructor(RoundTripConstructor):
    yaml_constructors: ClassVar[dict[Any, Any]] = ...

    def construct_mapping(  # type: ignore[override]
        self,
        node: Any,
        maptyp: Any,
        deep: bool | None = False,
    ) -> None: ...

class StrictYAMLScanner(RoundTripScanner):
    def check_token(self, *choices: Any) -> bool: ...

class StrictYAMLLoader(
    Reader,
    StrictYAMLScanner,
    RoundTripParser,
    Composer,
    StrictYAMLConstructor,
    VersionedResolver,
):
    def __init__(
        self,
        stream: Any,
        version: VersionType | None = None,  # pyright: ignore[reportInvalidTypeForm]
        preserve_quotes: bool | None = None,
    ) -> None: ...

def as_document(
    data: Any,
    schema: Validator | None = None,
    label: str | None = ...,
) -> YAML: ...
def generic_load(
    yaml_string: Any,
    schema: Validator | None = None,
    label: str | None = ...,
    allow_flow_style: bool | None = False,
) -> YAML: ...
def dirty_load(
    yaml_string: Any,
    schema: Validator | None = None,
    label: str | None = ...,
    allow_flow_style: bool | None = False,
) -> YAML: ...
def load(
    yaml_string: Any,
    schema: Validator | None = None,
    label: str | None = ...,
) -> YAML: ...
