from typing import Final

__all__ = (
    "BOOL_VALUES",
    "FALSE_VALUES",
    "TRUE_VALUES",
    "REGEXES",
)

TRUE_VALUES: Final[list[str]]
FALSE_VALUES: Final[list[str]]
BOOL_VALUES: list[str]
# Should be a types.MappingProxyType, not dict
REGEXES: dict[str, str]
