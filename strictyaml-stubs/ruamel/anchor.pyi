from typing import (
    Any,
    ClassVar,
    Final,
)

anchor_attrib: Final[str]

__all__ = ("Anchor",)

class Anchor:
    __slots__ = ("value", "always_dump")
    attrib: ClassVar[str] = "_yaml_anchor"
    value: Any | None
    always_dump: bool

    def __init__(self) -> None: ...
