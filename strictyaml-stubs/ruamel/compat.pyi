from abc import abstractmethod
from builtins import type as _type
from collections.abc import MutableSequence
from typing import (
    Any,
    BinaryIO,
    Final,
    TextIO,
)

from typing_extensions import TypeAlias

_DEFAULT_YAML_VERSION: Final[tuple[int, int]]
PY2: bool
PY3: bool

def utf8(s: str) -> str: ...
def to_str(s: str) -> str: ...
def to_unicode(s: str) -> str: ...

string_types: _type
integer_types: _type
class_types: _type
text_type: _type
binary_type: _type
MAXSIZE: int
unichr: _type
StringIO: TextIO
BytesIO: BinaryIO

no_limit_int: TypeAlias = int  # noqa: Y042

StreamType: TypeAlias = Any
StreamTextType: TypeAlias = TextIO | Any
VersionType: TypeAlias = list[int] | str | tuple[int, int]

builtins_module: Final[str]
UNICODE_SIZE: int

def with_metaclass(meta: Any, *bases: Any) -> Any: ...

DBG_TOKEN: int
DBG_EVENT: int
DBG_NODE: int

_debug: int | None
_debugx: str | None

class ObjectCounter:
    def __init__(self) -> None: ...
    def __call__(self, k: Any) -> None: ...
    def dump(self) -> None: ...

object_counter: ObjectCounter

def dbg(val: Any | None = None) -> Any: ...

class Nprint:
    def __init__(self, file_name: Any | None = None) -> None: ...
    def __call__(self, *args: Any, **kw: Any) -> None: ...
    def set_max_print(self, i: int) -> None: ...

nprint: Nprint
nprintf: Nprint

def check_namespace_char(ch: str) -> bool: ...
def check_anchorname_char(ch: str) -> bool: ...
def version_tnf(t1: Any, t2: Any | None = None) -> bool | None: ...

class MutableSliceableSequence(MutableSequence):  # type: ignore
    __slots__ = ()

    def __getitem__(self, index: Any) -> Any: ...
    def __setitem__(self, index: Any, value: Any) -> Any: ...
    def __delitem__(self, index: Any) -> None: ...
    @abstractmethod
    def __getsingleitem__(self, index: Any) -> Any: ...
    @abstractmethod
    def __setsingleitem__(self, index: Any, value: Any) -> None: ...
    @abstractmethod
    def __delsingleitem__(self, index: Any) -> None: ...
