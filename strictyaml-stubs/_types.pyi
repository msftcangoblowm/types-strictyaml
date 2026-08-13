"""
.. moduleauthor:: Dave Faulkmore <https://mastodon.social/@msftcangoblowme>

Shared typing added by types-strictyaml

"""

import os
import types
from datetime import (
    date,
    datetime,
)
from decimal import Decimal
from typing import (
    Protocol,
    TypeAlias,
    TypeVar,
    runtime_checkable,
)

from strictyaml.ruamel.comments import (
    CommentedBase,
    CommentedMap,
    CommentedSeq,
)
from strictyaml.ruamel.scalarbool import ScalarBoolean
from strictyaml.ruamel.scalarfloat import ScalarFloat
from strictyaml.ruamel.scalarint import ScalarInt
from strictyaml.ruamel.scalarstring import ScalarString
from strictyaml.ruamel.timestamp import TimeStamp
from strictyaml.scalar import (
    Email,
    Regex,
    Str,
    Url,
)
from typing_extensions import Self

_AnyStr_co = TypeVar("_AnyStr_co", str, bytes, covariant=True)

__all__ = (
    "SEGMENT",
    "PathLikeStream",
    "ReadableFile",
    "StreamType",
    "StringKeyValidator",
    "YAMLChunkContents",
)

@runtime_checkable
class ReadableFile(Protocol[_AnyStr_co]):
    """Already-open file-like object.
    Supports ``read()`` and context management.
    """

    def read(self, size: int = -1) -> _AnyStr_co: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self,
        typ: type[BaseException] | None,
        value: BaseException | None,
        traceback: types.TracebackType | None,
    ) -> None: ...

@runtime_checkable
class PathLikeStream(Protocol):
    """Objects like pathlib.Path that must be opened first.
    Does NOT have ``read()``, but have ``open()`` which returns a file object.
    """

    def open(
        self,
        mode: str = "r",
        buffering: int = -1,
        encoding: str | None = None,
        errors: str | None = None,
        newline: str | None = None,
    ) -> ReadableFile[str] | ReadableFile[bytes]: ...

# PathLike, str, bytes, and IO variants
StreamType: TypeAlias = (
    str
    | bytes
    | os.PathLike[str]
    | os.PathLike[bytes]
    # Custom objects with ``.open()`` (e.g. pathlib.Path)
    | PathLikeStream
    # Already open file-like objects (io.TextIOBase, io.BytesIO, etc.)
    | ReadableFile[str]
    | ReadableFile[bytes]
)

YAMLChunkContents: TypeAlias = (
    CommentedBase
    # Specialized Scalars (Subclasses of CommentedBase or str)
    | TimeStamp  # Subclass of datetime.datetime
    | ScalarFloat  # Subclass of float
    | ScalarInt  # Subclass of int
    | ScalarBoolean  # Subclass of bool
    | ScalarString  # Subclass of str
    # Native Python Types (for untagged or strictly validated scalars)
    | str
    | int
    | float
    | bool
    | datetime  # Includes TimeStamp
    | date  # Parsed from YYYY-MM-DD
    | Decimal
    | type[None]
)

# Not CommentedBase, e.g. s.compound.UniqueSeq forces CommentedSet --> CommentedSeq
SEGMENT: TypeAlias = CommentedMap | CommentedSeq

# Convenience alias for built-in string-like validators (a "String-like"
# ScalarValidator). Does not include custom string-like ScalarValidators
# (e.g., Slug, XPathValidator).
#
# Represents practical validators usable with ``strictyaml.compound.Map._key_validator``
# for standard schemas.
#
# For library internals and especially for compatibility with custom string-like
# ScalarValidators, use ScalarValidator directly.
StringKeyValidator: TypeAlias = Str | Url | Email | Regex  # noqa: F841
