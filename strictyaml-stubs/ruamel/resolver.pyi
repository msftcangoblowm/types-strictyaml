from collections.abc import Callable
from typing import (
    Any,
    ClassVar,
)

from typing_extensions import TypeAlias

from .compat import VersionType
from .error import YAMLError
from .util import LazyEval

# Since LazyEval isn't generic, just alias the wrapper type itself
RegExpType: TypeAlias = LazyEval

__all__ = ["BaseResolver", "Resolver", "VersionedResolver"]

implicit_resolvers: list[
    tuple[list[tuple[int, int]], str, Callable[..., RegExpType], list[str]]
]

class ResolverError(YAMLError): ...

class BaseResolver:
    DEFAULT_SCALAR_TAG: ClassVar[str]
    DEFAULT_SEQUENCE_TAG: ClassVar[str]
    DEFAULT_MAPPING_TAG: ClassVar[str]

    yaml_implicit_resolvers: ClassVar[dict[Any, Any]]
    yaml_path_resolvers: ClassVar[dict[Any, Any]]

    loadumper: Any | None
    _loader_version: Any | None
    resolver_exact_paths: list[Any]
    resolver_prefix_paths: list[Any]

    def __init__(self, loadumper: Any | None = None) -> None: ...
    @property
    def parser(self) -> Any: ...
    @classmethod
    def add_implicit_resolver_base(
        cls,
        tag: Any,
        regexp: Any,
        first: str | None,
    ) -> None: ...
    @classmethod
    def add_implicit_resolver(
        cls,
        tag: Any,
        regexp: Any,
        first: str | None,
    ) -> None: ...
    @classmethod
    def add_path_resolver(
        cls,
        tag: Any,
        path: Any,
        kind: type | None = None,
    ) -> None: ...
    def descend_resolver(self, current_node: Any, current_index: Any) -> None: ...
    def ascend_resolver(self) -> None: ...
    def check_resolver_prefix(
        self,
        depth: int,
        path: str,
        kind: Any,
        current_node: Any,
        current_index: Any,
    ) -> bool: ...
    def resolve(self, kind: type, value: Any, implicit: Any) -> Any: ...
    # default implementation. rtype match with VersionedResolver.processing_version
    @property
    def processing_version(self) -> Any: ...

class Resolver(BaseResolver): ...

class VersionedResolver(BaseResolver):
    def __init__(
        self,
        version: VersionType | None = None,
        loader: Any | None = None,
        loadumper: Any | None = None,
    ) -> None: ...
    def add_version_implicit_resolver(
        self,
        version: VersionType,
        tag: Any,
        regexp: Any,
        first: str | None,
    ) -> None: ...
    def get_loader_version(self, version: VersionType | None) -> Any: ...
    @property
    def versioned_resolver(self) -> Any: ...
    def resolve(self, kind: type, value: Any, implicit: Any) -> Any: ...
    @property
    def processing_version(self) -> Any: ...
