from typing import Any

from typing_extensions import TypeAlias

from .compat import (
    StreamTextType,
    VersionType,
)
from .constructor import (
    BaseConstructor,
    Constructor,
    SafeConstructor,
)
from .main import (
    CEmitter,
    CParser,
)
from .representer import (
    BaseRepresenter,
    Representer,
    SafeRepresenter,
)
from .resolver import (
    BaseResolver,
    Resolver,
)

__all__ = [
    "CBaseLoader",
    "CSafeLoader",
    "CLoader",
    "CBaseDumper",
    "CSafeDumper",
    "CDumper",
]

StreamType: TypeAlias = Any

class CBaseLoader(CParser, BaseConstructor, BaseResolver):  # type: ignore
    def __init__(
        self,
        stream: StreamTextType,
        version: VersionType | None = None,
        preserve_quotes: bool | None = None,
    ) -> None: ...

class CSafeLoader(CParser, SafeConstructor, Resolver):  # type: ignore
    def __init__(
        self,
        stream: StreamTextType,
        version: VersionType | None = None,
        preserve_quotes: bool | None = None,
    ) -> None: ...

class CLoader(CParser, Constructor, Resolver):  # type: ignore
    def __init__(
        self,
        stream: StreamTextType,
        version: VersionType | None = None,
        preserve_quotes: bool | None = None,
    ) -> None: ...

class CBaseDumper(CEmitter, BaseRepresenter, BaseResolver):  # type: ignore
    def __init__(
        self,
        stream: StreamType,
        default_style: Any | None = None,
        default_flow_style: Any | None = None,
        canonical: Any | None = None,
        indent: bool | None = None,
        width: int | None = None,
        allow_unicode: int | None = None,
        line_break: bool | None = None,
        encoding: Any | None = None,
        explicit_start: Any | None = None,
        explicit_end: bool | None = None,
        version: Any = None,
        tags: Any | None = None,
        block_seq_indent: Any | None = None,
        top_level_colon_align: Any | None = None,
        prefix_colon: Any | None = None,
    ) -> None: ...

class CSafeDumper(CEmitter, SafeRepresenter, Resolver):  # type: ignore
    def __init__(
        self,
        stream: StreamType,
        default_style: Any | None = None,
        default_flow_style: Any | None = None,
        canonical: Any | None = None,
        indent: bool | None = None,
        width: int | None = None,
        allow_unicode: int | None = None,
        line_break: bool | None = None,
        encoding: Any | None = None,
        explicit_start: Any | None = None,
        explicit_end: bool | None = None,
        version: bool | None = None,
        tags: Any | None = None,
        block_seq_indent: Any | None = None,
        top_level_colon_align: Any | None = None,
        prefix_colon: Any | None = None,
    ) -> None: ...

class CDumper(CEmitter, Representer, Resolver):  # type: ignore
    def __init__(
        self,
        stream: StreamType,
        default_style: Any | None = None,
        default_flow_style: Any | None = None,
        canonical: Any | None = None,
        indent: bool | None = None,
        width: int | None = None,
        allow_unicode: int | None = None,
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
