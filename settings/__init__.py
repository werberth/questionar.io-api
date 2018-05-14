from .base import *

# Load a `local.py` module, if it exists
try:
    from .local import *
except ImportError:
    pass
