from typing import (
    Any,
    ClassVar,
)

__all__ = (
    "CollectionNode",
    "MappingNode",
    "Node",
    "ScalarNode",
    "SequenceNode",
)

class Node:
    __slots__ = ("tag", "value", "start_mark", "end_mark", "comment", "anchor")
    def __init__(
        self,
        tag: Any,
        value: Any,  # string_types | tuple | Self
        start_mark: Any,
        end_mark: Any,
        comment: str | None = None,
        anchor: Any | None = None,
    ) -> None: ...
    def dump(self, indent: int = 0) -> None: ...

class ScalarNode(Node):
    __slots__ = ("style",)
    id: ClassVar[str]

    def __init__(
        self,
        tag: Any,
        value: Any,
        start_mark: Any | None = None,
        end_mark: Any | None = None,
        style: Any | None = None,
        comment: str | None = None,
        anchor: Any | None = None,
    ) -> None: ...

class CollectionNode(Node):
    __slots__ = ("flow_style",)

    def __init__(
        self,
        tag: Any,
        value: Any,
        start_mark: Any | None = None,
        end_mark: Any | None = None,
        flow_style: Any | None = None,
        comment: str | None = None,
        anchor: Any | None = None,
    ) -> None: ...

class SequenceNode(CollectionNode):
    __slots__ = ()
    id: ClassVar[str]

class MappingNode(CollectionNode):
    __slots__ = ("merge",)
    id: ClassVar[str] = "mapping"

    def __init__(
        self,
        tag: Any,
        value: Any,
        start_mark: Any | None = None,
        end_mark: Any | None = None,
        flow_style: Any | None = None,
        comment: str | None = None,
        anchor: Any | None = None,
    ) -> None: ...
