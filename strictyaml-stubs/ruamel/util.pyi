import re
from collections.abc import Callable
from typing import Any

from typing_extensions import TypeAlias

from .._types import ReadableFile  # isort: skip

__all__ = ("RegExp", "load_yaml_guess_indent", "configobj_walker")

class LazyEval:
    def __init__(
        self,
        func: Callable[..., Any],
        *args: Any,
        **kwargs: Any,
    ) -> None: ...
    def __getattribute__(self, name: Any) -> Any: ...
    def __setattr__(self, name: Any, value: Any) -> None: ...

# Define the TypeAlias as the target type (what LazyEval proxies to)
# Since RegExp wraps re.compile, the effective type is Pattern[str]
PatternStr: TypeAlias = re.Pattern[str]

# Since LazyEval isn't generic, just alias the wrapper type itself
RegExpType: TypeAlias = LazyEval

RegExp: Callable[..., RegExpType]

r"""  # noqa: Y021
def compile_regex(pattern: str) -> LazyEval:
    return RegExp(pattern)

# Usage
regex_instance: PatternStr = compile_regex(r"\d+")
# Note: You might still need # type: ignore if mypy doesn't understand the proxy
# A safer explicit annotation for the wrapper itself is just LazyEval:
regex_wrapper: LazyEval = compile_regex(r"\d+")
"""

def load_yaml_guess_indent(
    stream: ReadableFile[str] | ReadableFile[bytes],
    **kw: Any,
) -> Any: ...
def configobj_walker(cfg: Any) -> Any: ...
def _walk_section(s: Any, level: int = 0) -> Any: ...
