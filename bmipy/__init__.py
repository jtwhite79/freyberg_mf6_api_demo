from ._version import get_versions
from .bmi import Bmi

__all__ = ["Bmi"]

__version__ = get_versions()["version"]
del get_versions
