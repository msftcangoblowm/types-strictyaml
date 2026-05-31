from typing import (
    Any,
    ClassVar,
    Final,
)

from .error import StreamMark

SHOWLINES: Final[bool]

class Token:
    __slots__ = ("start_mark", "end_mark", "_comment")

    def __init__(self, start_mark: StreamMark, end_mark: StreamMark) -> None: ...
    def add_post_comment(self, comment: Any) -> None: ...
    def add_pre_comments(self, comments: Any) -> None: ...
    def get_comment(self) -> Any: ...
    @property
    def comment(self) -> Any: ...
    def move_comment(self, target: Any, empty: bool = False) -> Any: ...
    def split_comment(self) -> Any: ...

class DirectiveToken(Token):
    __slots__ = ("name", "value")
    id: ClassVar[str]

    def __init__(
        self,
        name: Any,
        value: Any,
        start_mark: Any,
        end_mark: Any,
    ) -> None: ...

class DocumentStartToken(Token):
    __slots__ = ()
    id: ClassVar[str]

class DocumentEndToken(Token):
    __slots__ = ()
    id: ClassVar[str]

class StreamStartToken(Token):
    __slots__ = ("encoding",)
    id: ClassVar[str]

    def __init__(
        self,
        start_mark: Any | None = None,
        end_mark: Any | None = None,
        encoding: Any | None = None,
    ) -> None: ...

class StreamEndToken(Token):
    __slots__ = ()
    id: ClassVar[str]

class BlockSequenceStartToken(Token):
    __slots__ = ()
    id: ClassVar[str]

class BlockMappingStartToken(Token):
    __slots__ = ()
    id: ClassVar[str]

class BlockEndToken(Token):
    __slots__ = ()
    id: ClassVar[str]

class FlowSequenceStartToken(Token):
    __slots__ = ()
    id: ClassVar[str]

class FlowMappingStartToken(Token):
    __slots__ = ()
    id: ClassVar[str]

class FlowSequenceEndToken(Token):
    __slots__ = ()
    id: ClassVar[str]

class FlowMappingEndToken(Token):
    __slots__ = ()
    id: ClassVar[str]

class KeyToken(Token):
    __slots__ = ()
    id: ClassVar[str]

class ValueToken(Token):
    __slots__ = ()
    id: ClassVar[str]

class BlockEntryToken(Token):
    __slots__ = ()
    id: ClassVar[str]

class FlowEntryToken(Token):
    __slots__ = ()
    id: ClassVar[str]

class AliasToken(Token):
    __slots__ = ("value",)
    id: ClassVar[str]

    def __init__(
        self,
        value: Any,
        start_mark: Any,
        end_mark: Any,
    ) -> None: ...

class AnchorToken(Token):
    __slots__ = ("value",)
    id: ClassVar[str]

    def __init__(
        self,
        value: Any,
        start_mark: Any,
        end_mark: Any,
    ) -> None: ...

class TagToken(Token):
    __slots__ = ("value",)
    id: ClassVar[str]

    def __init__(
        self,
        value: Any,
        start_mark: Any,
        end_mark: Any,
    ) -> None: ...

class ScalarToken(Token):
    __slots__ = ("value", "plain", "style")
    id: ClassVar[str]

    def __init__(
        self,
        value: Any,
        plain: Any,
        start_mark: Any,
        end_mark: Any,
        style: Any | None = None,
    ) -> None: ...

class CommentToken(Token):
    __slots__ = ("value", "pre_done")
    id: ClassVar[str]

    def __init__(
        self,
        value: Any,
        start_mark: Any,
        end_mark: Any,
    ) -> None: ...
    def reset(self) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
