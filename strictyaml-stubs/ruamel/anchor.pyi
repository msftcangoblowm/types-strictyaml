from typing import (
    ClassVar,
    Final,
)

anchor_attrib: Final[str]

__all__ = ("Anchor",)

class Anchor:
    __slots__ = ("value", "always_dump")
    attrib: ClassVar[str]

    def __init__(self) -> None: ...
