from typing import Any

from strictyaml.ruamel.compat import VersionType
from strictyaml.ruamel.emitter import Emitter
from strictyaml.ruamel.representer import RoundTripRepresenter
from strictyaml.ruamel.resolver import BaseResolver
from strictyaml.ruamel.serializer import Serializer

from ._types import StreamType  # isort: skip

__all__ = ("StrictYAMLDumper",)

class StrictYAMLResolver(BaseResolver):
    def __init__(
        self,
        version: VersionType | None = None,
        loader: Any | None = None,
    ) -> None: ...

class StrictYAMLDumper(Emitter, Serializer, RoundTripRepresenter, StrictYAMLResolver):
    def __init__(
        self,
        stream: StreamType,
        default_style: Any | None = None,
        default_flow_style: Any | None = None,
        canonical: Any | None = None,
        indent: int | None = None,
        width: int | None = None,
        allow_unicode: bool | None = None,
        line_break: Any | None = None,
        encoding: Any | None = None,
        explicit_start: bool | None = None,
        explicit_end: bool | None = None,
        version: VersionType | None = None,
        tags: Any | None = None,
        block_seq_indent: int | None = None,
        top_level_colon_align: bool | None = None,
        prefix_colon: Any | None = None,
    ) -> None: ...
