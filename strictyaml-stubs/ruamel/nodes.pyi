from typing import (
    Any,
    ClassVar,
)

from typing_extensions import Self

from .anchor import Anchor

__all__ = (
    "CollectionNode",
    "MappingNode",
    "Node",
    "ScalarNode",
    "SequenceNode",
)

class Node:
    __slots__ = ("tag", "value", "start_mark", "end_mark", "comment", "anchor")
    tag: Any
    value: str | tuple[Self, ...] | Self | Any
    start_mark: Any
    end_mark: Any
    comment: str | None
    anchor: Anchor | None

    def __init__(
        self,
        tag: Any,
        value: str | tuple[Self, ...] | Self | Any,  # Any is undesirable junk
        start_mark: Any,
        end_mark: Any,
        comment: str | None = None,
        anchor: Anchor | None = None,
    ) -> None: ...
    def dump(self, indent: int = 0) -> None: ...

class ScalarNode(Node):
    __slots__ = ("style",)
    id: ClassVar[str]
    style: Any | None

    def __init__(
        self,
        tag: Any,
        value: Any,
        start_mark: Any | None = None,
        end_mark: Any | None = None,
        style: Any | None = None,
        comment: str | None = None,
        anchor: Anchor | None = None,
    ) -> None: ...

class CollectionNode(Node):
    __slots__ = ("flow_style",)
    flow_style: Any | None

    def __init__(
        self,
        tag: Any,
        value: Any,
        start_mark: Any | None = None,
        end_mark: Any | None = None,
        flow_style: Any | None = None,
        comment: str | None = None,
        anchor: Anchor | None = None,
    ) -> None: ...

class SequenceNode(CollectionNode):
    __slots__ = ()
    id: ClassVar[str]

class MappingNode(CollectionNode):
    __slots__ = ("merge",)
    id: ClassVar[str] = "mapping"
    # exact typing?
    merge: Any | None

    def __init__(
        self,
        tag: Any,
        value: Any,
        start_mark: Any | None = None,
        end_mark: Any | None = None,
        flow_style: Any | None = None,
        comment: str | None = None,
        anchor: Anchor | None = None,
    ) -> None: ...
