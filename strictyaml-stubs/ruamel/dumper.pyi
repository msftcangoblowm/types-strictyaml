from typing import Any

from typing_extensions import TypeAlias

from .emitter import Emitter
from .representer import (
    BaseRepresenter,
    Representer,
    RoundTripRepresenter,
    SafeRepresenter,
)
from .resolver import (
    BaseResolver,
    Resolver,
    VersionedResolver,
)
from .serializer import Serializer

__all__ = ["BaseDumper", "SafeDumper", "Dumper", "RoundTripDumper"]

StreamType: TypeAlias = Any

class BaseDumper(Emitter, Serializer, BaseRepresenter, BaseResolver):
    def __init__(
        self,
        stream: Any,
        default_style: StreamType | None = None,
        default_flow_style: Any | None = None,
        canonical: Any | None = None,
        indent: bool | None = None,
        width: int | None = None,
        allow_unicode: int | None = None,
        line_break: bool | None = None,
        encoding: Any | None = None,
        explicit_start: Any | None = None,
        explicit_end: bool | None = None,
        version: Any | None = None,
        tags: Any | None = None,
        block_seq_indent: Any | None = None,
        top_level_colon_align: Any | None = None,
        prefix_colon: Any | None = None,
    ) -> None: ...

class SafeDumper(Emitter, Serializer, SafeRepresenter, Resolver):
    def __init__(
        self,
        stream: StreamType,
        default_style: Any | None = None,
        default_flow_style: Any | None = None,
        canonical: bool | None = None,
        indent: int | None = None,
        width: int | None = None,
        allow_unicode: bool | None = None,
        line_break: Any | None = None,
        encoding: Any | None = None,
        explicit_start: bool | None = None,
        explicit_end: bool | None = None,
        version: Any | None = None,
        tags: Any | None = None,
        block_seq_indent: Any | None = None,
        top_level_colon_align: Any | None = None,
        prefix_colon: Any | None = None,
    ) -> None: ...

class Dumper(Emitter, Serializer, Representer, Resolver):
    def __init__(
        self,
        stream: StreamType,
        default_style: Any | None = None,
        default_flow_style: Any | None = None,
        canonical: bool | None = None,
        indent: int | None = None,
        width: int | None = None,
        allow_unicode: bool | None = None,
        line_break: Any | None = None,
        encoding: Any | None = None,
        explicit_start: bool | None = None,
        explicit_end: bool | None = None,
        version: Any | None = None,
        tags: Any | None = None,
        block_seq_indent: Any | None = None,
        top_level_colon_align: Any | None = None,
        prefix_colon: Any | None = None,
    ) -> None: ...

class RoundTripDumper(Emitter, Serializer, RoundTripRepresenter, VersionedResolver):
    def __init__(
        self,
        stream: StreamType,
        default_style: Any | None = None,
        default_flow_style: bool | None = None,
        canonical: int | None = None,
        indent: int | None = None,
        width: int | None = None,
        allow_unicode: bool | None = None,
        line_break: Any | None = None,
        encoding: Any | None = None,
        explicit_start: bool | None = None,
        explicit_end: bool | None = None,
        version: Any | None = None,
        tags: Any | None = None,
        block_seq_indent: Any | None = None,
        top_level_colon_align: Any | None = None,
        prefix_colon: Any | None = None,
    ) -> None: ...
