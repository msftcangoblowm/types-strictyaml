from collections.abc import Callable
from typing import Any

from .anchor import Anchor

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
    start_mark: Any | None
    end_mark: Any | None
    comment: Callable[[], None] | None

    # explicit case comment=None not handled
    def __init__(
        self,
        start_mark: Any | None = None,
        end_mark: Any | None = None,
        comment: Callable[[], None] | None = ...,
    ) -> None: ...

class NodeEvent(Event):
    __slots__ = ("anchor",)
    anchor: Anchor

    # lacks input validation for Anchor
    def __init__(
        self,
        anchor: Anchor,
        start_mark: Any | None = None,
        end_mark: Any | None = None,
        comment: Any | None = None,
    ) -> None: ...

class CollectionStartEvent(NodeEvent):
    __slots__ = ("tag", "implicit", "flow_style", "nr_items")
    tag: Any
    implicit: Any
    flow_style: Any | None
    nr_items: int | None

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
    encoding: Any | None

    # encoding lacks input validation
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
    explicit: Any | None
    version: Any | None
    tags: Any | None

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
    explicit: Any | None

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
    tag: Any
    implicit: Any
    value: Any
    style: Any | None

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
