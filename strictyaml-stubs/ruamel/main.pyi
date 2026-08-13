import types
from pathlib import Path
from typing import (
    Any,
    Final,
)

from typing_extensions import TypeAlias

from .compat import VersionType
from .composer import Composer as Composer_
from .constructor import BaseConstructor as BaseConstructor_
from .constructor import Constructor as Constructor_
from .constructor import RoundTripConstructor as RoundTripConstructor_
from .constructor import SafeConstructor as SafeConstructor_
from .emitter import Emitter as Emitter_
from .parser import Parser as Parser_
from .parser import RoundTripParser as RoundTripParser_
from .reader import Reader as Reader_
from .representer import BaseRepresenter as BaseRepresenter_
from .representer import Representer as Representer_
from .representer import SafeRepresenter as SafeRepresenter_
from .resolver import VersionedResolver as VersionedResolver_
from .scanner import RoundTripScanner as RoundTripScanner_
from .scanner import Scanner as Scanner_
from .serializer import Serializer as Serializer_

from .._types import ReadableFile, StreamType  # isort: skip

# isort: off
try:
    # New name for clibz
    # pip install ruamel.yaml.clibz
    from _ruamel_yaml_clibz import (  # type: ignore[import-not-found]
        CEmitter,  # pyright: ignore[reportUnknownVariableType,reportRedeclaration]
    )
    from _ruamel_yaml_clibz import (  # type: ignore[import-not-found, unused-ignore]
        CParser,  # pyright: ignore[reportUnknownVariableType,reportRedeclaration]
    )
except ImportError:
    try:
        # Legacy name for clib
        # pip install ruamel.yaml.clib
        from _ruamel_yaml import (  # type: ignore[import-not-found]
            CEmitter,  # pyright: ignore[reportUnknownVariableType,reportRedeclaration]
        )
        from _ruamel_yaml import (  # type: ignore[import-not-found, unused-ignore]
            CParser,  # type: ignore[unused-ignore]  # pyright: ignore[reportUnknownVariableType,reportRedeclaration]  # fmt: skip
        )
    except ImportError:
        # Fallback to pure Python
        CParser: TypeAlias = None  # type: ignore[no-redef]
        CEmitter: TypeAlias = None  # type: ignore[no-redef]
# isort: on

enforce: Final[Any]
enc: str | None

# .tokens
SHOWLINES: bool

__all__ = ("CParser", "CEmitter", "YAML", "YAMLObject")

class YAMLContextManager:
    def __init__(self, yaml: Any, transform: Any | None = None) -> None: ...
    def teardown_output(self) -> None: ...
    def init_output(self, first_data: Any) -> None: ...
    def dump(self, data: Any) -> None: ...

class YAML:
    Composer: Composer_ | None
    Constructor: (
        Constructor_
        | BaseConstructor_
        | SafeConstructor_
        | RoundTripConstructor_
        | None
    )
    Emitter: Emitter_
    Parser: Parser_ | RoundTripParser_ | None
    Reader: Reader_ | None
    Representer: Representer_ | BaseRepresenter_ | SafeRepresenter_ | None
    # get_serializer_representer_emitter uses BaseResolver and Resolver
    Resolver: VersionedResolver_
    Scanner: Scanner_ | RoundTripScanner_ | None
    Serializer: Serializer_ | None
    # unlikely to be set to a different contextmanager
    _context_manager: YAMLContextManager | None
    _output: Path | Any | None
    allow_unicode: bool | None
    default_flow_style: bool | None
    plug_ins: list[Any]
    # unused
    pure: bool | None
    typ: list[Any] | Any

    # #####
    # Did not confirm the rest
    # #####
    stream: StreamType | None
    canonical: Any | None
    old_indent: Any | None
    width: Any | None
    line_break: Any | None
    map_indent: Any | None
    sequence_indent: Any | None
    sequence_dash_offset: Any | int
    compact_seq_seq: Any | None
    compact_seq_map: Any | None
    sort_base_mapping_type_on_output: Any | None  # default: sort
    top_level_colon_align: Any | None
    prefix_colon: Any | None
    version: Any | None
    preserve_quotes: Any | None
    allow_duplicate_keys: bool = False  # duplicate keys in map, set
    encoding: str | None
    explicit_start: Any | None
    explicit_end: Any | None
    tags: Any | None
    default_style: Any | None
    top_level_block_style_scalar_no_indent_error_1_1: bool
    # directives end indicator with single scalar document
    scalar_after_indicator: Any | None
    # [a, b: 1, c: {d: 2}]  vs. [a, {b: 1}, {c: {d: 2}}]
    brace_single_entry_mapping_in_flow_sequence: bool = False

    def __init__(
        self,
        _kw: Any = ...,
        typ: str | None = None,
        pure: bool | None = False,  # lacks input validation
        output: Any | None = None,
        plug_ins: Any | None = None,
    ) -> None: ...
    @property
    def reader(self) -> Any: ...
    @property
    def scanner(self) -> Any: ...
    @property
    def parser(self) -> Any: ...
    @property
    def composer(self) -> Any: ...
    @property
    def constructor(self) -> Any: ...
    @property
    def resolver(self) -> Any: ...
    @property
    def emitter(self) -> Any: ...
    @property
    def serializer(self) -> Any: ...
    @property
    def representer(self) -> Any: ...
    def load(self, stream: StreamType) -> Any: ...
    def load_all(self, stream: StreamType, _kw: Any | None = ...) -> Any: ...
    def get_constructor_parser(
        self,
        stream: ReadableFile[str] | ReadableFile[bytes],
    ) -> Any: ...
    def dump(
        self,
        data: Any,
        stream: StreamType | None = None,
        _kw: Any | None = ...,
        transform: Any | None = None,
    ) -> Any: ...
    def dump_all(
        self,
        documents: Any,
        stream: StreamType,
        _kw: Any | None = ...,
        transform: Any | None = ...,
    ) -> Any: ...
    def Xdump_all(
        self,
        documents: Any,
        stream: StreamType,
        _kw: Any | None = ...,
        transform: Any | None = None,
    ) -> Any: ...
    def get_serializer_representer_emitter(
        self,
        stream: StreamType,
        tlca: Any,
    ) -> Any: ...
    def map(self, **kw: Any) -> Any: ...
    def seq(self, *args: Any) -> Any: ...
    def official_plug_ins(self) -> Any: ...
    def register_class(self, cls: Any) -> Any: ...
    def parse(
        self,
        stream: ReadableFile[str] | ReadableFile[bytes],
    ) -> Any: ...
    def __enter__(self) -> Any: ...
    def __exit__(
        self,
        typ: type[BaseException] | None,
        value: BaseException | None,
        traceback: types.TracebackType | None,
    ) -> None: ...
    @property
    def indent(self) -> Any: ...
    @indent.setter
    def indent(self, val: Any) -> None: ...
    @property
    def block_seq_indent(self) -> Any: ...
    @block_seq_indent.setter
    def block_seq_indent(self, val: Any) -> None: ...
    def compact(
        self,
        seq_seq: Any | None = None,
        seq_map: Any | None = None,
    ) -> None: ...

def yaml_object(yml: Any) -> Any: ...
def scan(
    stream: ReadableFile[str] | ReadableFile[bytes],
    Loader: Any = ...,
) -> Any: ...
def parse(
    stream: ReadableFile[str] | ReadableFile[bytes],
    Loader: Any = ...,
) -> Any: ...
def compose(
    stream: ReadableFile[str] | ReadableFile[bytes],
    Loader: Any = ...,
) -> Any: ...
def compose_all(
    stream: ReadableFile[str] | ReadableFile[bytes],
    Loader: Any = ...,
) -> Any: ...
def load(
    stream: ReadableFile[str] | ReadableFile[bytes],
    Loader: Any | None = None,
    version: VersionType | None = None,
    preserve_quotes: Any | None = None,
) -> Any: ...
def load_all(
    stream: ReadableFile[str] | ReadableFile[bytes] | None,
    Loader: Any | None = None,
    version: VersionType | None = None,
    preserve_quotes: bool | None = None,
) -> Any: ...
def safe_load(
    stream: ReadableFile[str] | ReadableFile[bytes],
    version: VersionType | None = None,
) -> Any: ...
def safe_load_all(
    stream: ReadableFile[str] | ReadableFile[bytes],
    version: VersionType | None = None,
) -> Any: ...
def round_trip_load(
    stream: ReadableFile[str] | ReadableFile[bytes],
    version: VersionType | None = None,
    preserve_quotes: bool | None = None,
) -> Any: ...
def round_trip_load_all(
    stream: ReadableFile[str] | ReadableFile[bytes],
    version: VersionType | None = None,
    preserve_quotes: bool | None = None,
) -> Any: ...
def emit(
    events: Any,
    stream: StreamType | None = None,
    Dumper: Any = ...,
    canonical: bool | None = None,
    indent: int | None = None,
    width: int | None = None,
    allow_unicode: bool | None = None,
    line_break: Any | None = None,
) -> Any: ...
def serialize_all(
    nodes: Any,
    stream: StreamType | None = None,
    Dumper: Any | None = ...,
    canonical: Any | None = None,
    indent: int | None = None,
    width: int | None = None,
    allow_unicode: bool | None = None,
    line_break: Any | None = None,
    encoding: Any | None = ...,
    explicit_start: bool | None = None,
    explicit_end: bool | None = None,
    version: VersionType | None = None,
    tags: Any | None = None,
) -> Any: ...
def serialize(
    node: Any,
    stream: StreamType | None = None,
    Dumper: Any | None = ...,
    **kwds: Any | None,
) -> Any: ...
def dump_all(
    documents: Any,
    stream: StreamType | None = None,
    Dumper: Any | None = ...,
    default_style: Any | None = ...,
    default_flow_style: Any | None = ...,
    canonical: bool | None = None,
    indent: int | None = None,
    width: int | None = None,
    allow_unicode: bool | None = None,
    line_break: Any | None = None,
    encoding: Any | None = ...,
    explicit_start: bool | None = None,
    explicit_end: bool | None = None,
    version: Any | None = None,
    tags: Any | None = None,
    block_seq_indent: Any | None = None,
    top_level_colon_align: Any | None = None,
    prefix_colon: Any | None = None,
) -> str | None: ...
def dump(
    data: Any,
    stream: StreamType | None = None,
    Dumper: Any | None = ...,
    default_style: Any | None = ...,
    default_flow_style: Any | None = ...,
    canonical: bool | None = None,
    indent: int | None = None,
    width: int | None = None,
    allow_unicode: bool | None = None,
    line_break: Any | None = None,
    encoding: Any | None = ...,
    explicit_start: bool | None = None,
    explicit_end: bool | None = None,
    version: VersionType | None = None,
    tags: Any | None = None,
    block_seq_indent: Any | None = None,
) -> str | None: ...
def safe_dump_all(
    documents: Any,
    stream: StreamType | None = None,
    **kwds: Any,
) -> str | None: ...
def safe_dump(
    data: Any,
    stream: StreamType | None = None,
    **kwds: Any,
) -> str | None: ...
def round_trip_dump(
    data: Any,
    stream: StreamType | None = None,
    Dumper: Any | None = ...,
    default_style: Any | None = None,
    default_flow_style: Any | None = None,
    canonical: bool | None = None,
    indent: int | None = None,
    width: int | None = None,
    allow_unicode: bool | None = None,
    line_break: Any | None = None,
    encoding: Any | None = ...,
    explicit_start: bool | None = None,
    explicit_end: bool | None = None,
    version: VersionType | None = None,
    tags: Any | None = None,
    block_seq_indent: Any | None = None,
    top_level_colon_align: Any | None = None,
    prefix_colon: Any | None = None,
) -> str | None: ...
def add_implicit_resolver(
    tag: Any,
    regexp: Any,
    first: Any | None = None,
    Loader: Any | None = None,
    Dumper: Any | None = None,
    resolver: Any | None = ...,
) -> None: ...
def add_path_resolver(
    tag: Any,
    path: Any,
    kind: Any | None = None,
    Loader: Any | None = None,
    Dumper: Any | None = None,
    resolver: Any | None = ...,
) -> None: ...
def add_constructor(
    tag: Any,
    object_constructor: Any,
    Loader: Any | None = None,
    constructor: Any | None = ...,
) -> None: ...
def add_multi_constructor(
    tag_prefix: Any,
    multi_constructor: Any,
    Loader: Any | None = None,
    constructor: Any | None = ...,
) -> None: ...
def add_representer(
    data_type: Any,
    object_representer: Any,
    Dumper: Any | None = None,
    representer: Any | None = ...,
) -> None: ...
def add_multi_representer(
    data_type: Any,
    multi_representer: Any,
    Dumper: Any | None = None,
    representer: Any | None = ...,
) -> None: ...

class YAMLObjectMetaclass(type):
    def __init__(cls, name: Any, bases: Any, kwds: Any) -> None: ...

class YAMLObject(metaclass=YAMLObjectMetaclass):
    __slots__ = ()

    yaml_constructor: Any = ...
    yaml_representer: Any = ...

    yaml_tag: Any = None
    yaml_flow_style: Any = None

    @classmethod
    def from_yaml(cls, constructor: Any, node: Any) -> Any: ...
    @classmethod
    def to_yaml(cls, representer: Any, data: Any) -> Any: ...
