from typing import (
    Any,
    ClassVar,
)

from .compat import VersionType
from .error import YAMLError
from .util import RegExpType

__all__ = ("SerializerError", "Serializer", "templated_id")

class SerializerError(YAMLError): ...

class Serializer:
    ANCHOR_TEMPLATE: ClassVar[str]
    ANCHOR_RE: ClassVar[RegExpType]

    def __init__(
        self,
        encoding: Any | None = None,
        explicit_start: bool | None = None,
        explicit_end: bool | None = None,
        version: VersionType | None = None,
        tags: Any | None = None,
        dumper: Any | None = None,
    ) -> None: ...
    @property
    def emitter(self) -> Any: ...
    @property
    def resolver(self) -> Any: ...
    def open(self) -> None: ...
    def close(self) -> None: ...
    def serialize(self, node: Any) -> None: ...
    def anchor_node(self, node: Any) -> None: ...
    def generate_anchor(self, node: Any) -> Any: ...
    def serialize_node(self, node: Any, parent: Any, index: Any) -> None: ...

def templated_id(s: str) -> Any: ...
