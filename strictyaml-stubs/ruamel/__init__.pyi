from .error import YAMLError

# isort: off
from .main import SHOWLINES  # noqa: F401  # pyright: ignore[reportUnusedImport]
from .main import CEmitter  # noqa: F401  # type: ignore[unused-ignore]
from .main import CParser  # noqa: F401  # type: ignore[unused-ignore]
from .main import enc  # noqa: F401  # pyright: ignore[reportUnusedImport]
from .main import enforce  # noqa: F401  # pyright: ignore[reportUnusedImport]

# isort: on

PY3: bool
__with_libyaml__: bool

# setuptools-scm format would include: prerelease and local
version_info: tuple[int, int, int]  # , str, str

__all__ = ("YAMLError",)
