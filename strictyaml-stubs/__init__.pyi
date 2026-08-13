from typing import Final

from strictyaml import exceptions
from strictyaml.any_validator import Any
from strictyaml.compound import (
    FixedSeq,
    Map,
    MapCombined,
    MapPattern,
    Optional,
    Seq,
    UniqueSeq,
)

# Disallowed token exceptions
# Exceptions
from strictyaml.exceptions import (
    AnchorTokenDisallowed,
    DisallowedToken,
    DuplicateKeysDisallowed,
    FlowMappingDisallowed,
    StrictYAMLError,
    TagTokenDisallowed,
    YAMLValidationError,
)

# Document builder
# The all important loader
from strictyaml.parser import (
    as_document,
    dirty_load,
    load,
)

# YAML object
from strictyaml.representation import YAML

# Base exception from strictyaml.ruamel (all exceptions inherit from this)
from strictyaml.ruamel import YAMLError
from strictyaml.scalar import (
    Bool,
    CommaSeparated,
    Datetime,
    Decimal,
    Email,
    EmptyDict,
    EmptyList,
    EmptyNone,
    Enum,
    Float,
    HexInt,
    Int,
    NullNone,
    Regex,
    ScalarValidator,
    Str,
    Url,
)

# Validators
from strictyaml.validators import (
    OrValidator,
    Validator,
)

from ._types import (
    PathLikeStream,
    ReadableFile,
    StreamType,
)

__version__: Final[str]

__all__ = (
    "PathLikeStream",
    "ReadableFile",
    "StreamType",
    "load",
    "dirty_load",
    "as_document",
    "YAML",
    "Validator",
    "OrValidator",
    "Any",
    "ScalarValidator",
    "Enum",
    "Regex",
    "Email",
    "Url",
    "Str",
    "Int",
    "HexInt",
    "Bool",
    "Float",
    "Decimal",
    "Datetime",
    "CommaSeparated",
    "NullNone",
    "EmptyNone",
    "EmptyDict",
    "EmptyList",
    "Optional",
    "Map",
    "MapPattern",
    "MapCombined",
    "Seq",
    "UniqueSeq",
    "FixedSeq",
    "YAMLError",
    "StrictYAMLError",
    "YAMLValidationError",
    "DisallowedToken",
    "TagTokenDisallowed",
    "FlowMappingDisallowed",
    "AnchorTokenDisallowed",
    "DuplicateKeysDisallowed",
    "exceptions",
)
