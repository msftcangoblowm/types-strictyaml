import types
from pathlib import Path
from typing import (
    Any,
    Final,
)

from typing_extensions import TypeAlias

from .compat import (
    StreamTextType,
    VersionType,
    with_metaclass,
)

NoneType: TypeAlias = None
StreamType: TypeAlias = Any

CParser: NoneType = None
CEmitter: NoneType = None

enforce: Final[Any]

class YAML:
    def __init__(
        self,
        _kw: Any = ...,
        typ: str | None = None,
        pure: Any | None = None,
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
    def load(self, stream: Path | StreamTextType) -> Any: ...
    def load_all(self, stream: Path | StreamTextType, _kw: Any | None = ...) -> Any: ...
    def get_constructor_parser(self, stream: StreamTextType) -> Any: ...
    def dump(
        self,
        data: Any,
        stream: Path | StreamType = None,
        _kw: Any | None = ...,
        transform: Any | None = None,
    ) -> Any: ...
    def dump_all(
        self,
        documents: Any,
        stream: Path | StreamType,
        _kw: Any | None = ...,
        transform: Any | None = ...,
    ) -> Any: ...
    def Xdump_all(
        self,
        documents: Any,
        stream: Path | StreamType = None,
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
    def parse(self, stream: StreamTextType) -> Any: ...
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

class YAMLContextManager:
    def __init__(self, yaml: Any, transform: Any | None = None) -> None: ...
    def teardown_output(self) -> None: ...
    def init_output(self, first_data: Any) -> None: ...
    def dump(self, data: Any) -> None: ...

def yaml_object(yml: Any) -> Any: ...
def scan(stream: StreamTextType, Loader: Any = ...) -> Any: ...
def parse(stream: StreamTextType, Loader: Any = ...) -> Any: ...
def compose(stream: StreamTextType, Loader: Any = ...) -> Any: ...
def compose_all(stream: StreamTextType, Loader: Any = ...) -> Any: ...
def load(
    stream: StreamTextType,
    Loader: Any | None = None,
    version: VersionType | None = None,
    preserve_quotes: Any | None = None,
) -> Any: ...
def load_all(
    stream: StreamTextType | None,
    Loader: Any | None = None,
    version: VersionType | None = None,
    preserve_quotes: bool | None = None,
) -> Any: ...
def safe_load(stream: StreamTextType, version: VersionType | None = None) -> Any: ...
def safe_load_all(
    stream: StreamTextType, version: VersionType | None = None
) -> Any: ...
def round_trip_load(
    stream: StreamTextType,
    version: VersionType | None = None,
    preserve_quotes: bool | None = None,
) -> Any: ...
def round_trip_load_all(
    stream: StreamTextType,
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

class YAMLObject(with_metaclass(YAMLObjectMetaclass)):  # type: ignore
    __slots__ = ()

    yaml_constructor: Any = ...
    yaml_representer: Any = ...

    yaml_tag: Any = None
    yaml_flow_style: Any = None

    @classmethod
    def from_yaml(cls, constructor: Any, node: Any) -> Any: ...
    @classmethod
    def to_yaml(cls, representer: Any, data: Any) -> Any: ...
