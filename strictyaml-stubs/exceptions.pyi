from typing import (
    Any,
    ClassVar,
)

from strictyaml.ruamel.error import (
    MarkedYAMLError,
    StringMark,
)
from strictyaml.yamllocation import YAMLChunk

__all__ = (
    "CannotBuildDocumentFromInvalidData",
    "CannotBuildDocumentsFromEmptyDictOrList",
    "InvalidValidatorError",
    "StrictYAMLError",
    "YAMLSerializationError",
    "InvalidOptionalDefault",
    "YAMLValidationError",
    "DisallowedToken",
    "TagTokenDisallowed",
    "FlowMappingDisallowed",
    "AnchorTokenDisallowed",
    "DuplicateKeysDisallowed",
    "InconsistentIndentationDisallowed",
    "raise_type_error",
)

class StrictYAMLError(MarkedYAMLError): ...
class InvalidValidatorError(StrictYAMLError): ...
class CannotBuildDocumentFromInvalidData(StrictYAMLError): ...
class CannotBuildDocumentsFromEmptyDictOrList(StrictYAMLError): ...
class YAMLSerializationError(StrictYAMLError): ...
class InvalidOptionalDefault(YAMLSerializationError): ...

class YAMLValidationError(StrictYAMLError):
    context: Any
    problem: Any | None
    _chunk: YAMLChunk | None
    # This is a guess
    note: str | None

    def __init__(
        self,
        context: Any,
        problem: Any | None = None,
        chunk: YAMLChunk | None = None,
    ) -> None: ...
    @property
    def context_mark(self) -> StringMark: ...
    @property
    def problem_mark(self) -> StringMark: ...

class DisallowedToken(StrictYAMLError):
    MESSAGE: ClassVar[str] = ...

class TagTokenDisallowed(DisallowedToken):
    MESSAGE: ClassVar[str] = ...

class FlowMappingDisallowed(DisallowedToken):
    MESSAGE: ClassVar[str] = ...

class AnchorTokenDisallowed(DisallowedToken):
    MESSAGE: ClassVar[str] = ...

class DuplicateKeysDisallowed(DisallowedToken):
    MESSAGE: ClassVar[str] = ...

class InconsistentIndentationDisallowed(DisallowedToken):
    MESSAGE: ClassVar[str] = ...

def raise_type_error(yaml_object: Any, to_type: Any, alternatives: Any) -> None: ...
