from .compat import VersionType
from .composer import Composer
from .constructor import (
    BaseConstructor,
    Constructor,
    RoundTripConstructor,
    SafeConstructor,
)
from .parser import (
    Parser,
    RoundTripParser,
)
from .reader import Reader
from .resolver import VersionedResolver
from .scanner import (
    RoundTripScanner,
    Scanner,
)

from .._types import ReadableFile  # isort: skip

__all__ = ["BaseLoader", "SafeLoader", "Loader", "RoundTripLoader"]

class BaseLoader(Reader, Scanner, Parser, Composer, BaseConstructor, VersionedResolver):
    def __init__(
        self,
        stream: ReadableFile[str] | ReadableFile[bytes],
        version: VersionType | None = None,
        preserve_quotes: bool | None = None,
    ) -> None: ...

class SafeLoader(Reader, Scanner, Parser, Composer, SafeConstructor, VersionedResolver):
    def __init__(
        self,
        stream: ReadableFile[str] | ReadableFile[bytes],
        version: VersionType | None = None,
        preserve_quotes: bool | None = None,
    ) -> None: ...

class Loader(Reader, Scanner, Parser, Composer, Constructor, VersionedResolver):
    def __init__(
        self,
        stream: ReadableFile[str] | ReadableFile[bytes],
        version: VersionType | None = None,
        preserve_quotes: bool | None = None,
    ) -> None: ...

class RoundTripLoader(
    Reader,
    RoundTripScanner,
    RoundTripParser,
    Composer,
    RoundTripConstructor,
    VersionedResolver,
):
    def __init__(
        self,
        stream: ReadableFile[str] | ReadableFile[bytes],
        version: VersionType | None = None,
        preserve_quotes: bool | None = None,
    ) -> None: ...
