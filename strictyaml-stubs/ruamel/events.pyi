from collections.abc import Callable
from typing import Any

__all__ = (
    "AliasEvent",
    "CollectionStartEvent",
    "CollectionEndEvent",
    "CommentCheck",
    "DocumentStartEvent",
    "DocumentEndEvent",
    "Event",
    "MappingStartEvent",
    "MappingEndEvent",
    "NodeEvent",
    "ScalarEvent",
    "SequenceStartEvent",
    "SequenceEndEvent",
    "StreamStartEvent",
    "StreamEndEvent",
)

def CommentCheck() -> None: ...

class Event:
    __slots__ = ("start_mark", "end_mark", "comment")

    def __init__(
        self,
        start_mark: Any | None = None,
        end_mark: Any | None = None,
        comment: Callable[[], None] = ...,
    ) -> None: ...

class NodeEvent(Event):
    __slots__ = ("anchor",)

    def __init__(
        self,
        anchor: Any,
        start_mark: Any | None = None,
        end_mark: Any | None = None,
        comment: Any | None = None,
    ) -> None: ...

class CollectionStartEvent(NodeEvent):
    __slots__ = ("tag", "implicit", "flow_style", "nr_items")

    def __init__(
        self,
        anchor: Any,
        tag: Any,
        implicit: Any,
        start_mark: Any | None = None,
        end_mark: Any | None = None,
        flow_style: Any | None = None,
        comment: Any | None = None,
        nr_items: int | None = None,
    ) -> None: ...

class CollectionEndEvent(Event):
    __slots__ = ()

class StreamStartEvent(Event):
    __slots__ = ("encoding",)

    def __init__(
        self,
        start_mark: Any | None = None,
        end_mark: Any | None = None,
        encoding: Any | None = None,
        comment: Any | None = None,
    ) -> None: ...

class StreamEndEvent(Event):
    __slots__ = ()

class DocumentStartEvent(Event):
    __slots__ = ("explicit", "version", "tags")

    def __init__(
        self,
        start_mark: Any | None = None,
        end_mark: Any | None = None,
        explicit: Any | None = None,
        version: Any | None = None,
        tags: Any | None = None,
        comment: Any | None = None,
    ) -> None: ...

class DocumentEndEvent(Event):
    __slots__ = ("explicit",)

    def __init__(
        self,
        start_mark: Any | None = None,
        end_mark: Any | None = None,
        explicit: Any | None = None,
        comment: Any | None = None,
    ) -> None: ...

class AliasEvent(NodeEvent):
    __slots__ = ()

class ScalarEvent(NodeEvent):
    __slots__ = ("tag", "implicit", "value", "style")

    def __init__(
        self: Any,
        anchor: Any,
        tag: Any,
        implicit: Any,
        value: Any,
        start_mark: Any | None = None,
        end_mark: Any | None = None,
        style: Any | None = None,
        comment: Any | None = None,
    ) -> None: ...

class SequenceStartEvent(CollectionStartEvent):
    __slots__ = ()

class SequenceEndEvent(CollectionEndEvent):
    __slots__ = ()

class MappingStartEvent(CollectionStartEvent):
    __slots__ = ()

class MappingEndEvent(CollectionEndEvent):
    __slots__ = ()
