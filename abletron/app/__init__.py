from . import screens, widgets
from .screens import CSS_PATHS as SCREENS_CSS
from .widgets import CSS_PATHS as WIDGETS_CSS

CSS_PATHS = SCREENS_CSS + WIDGETS_CSS

__all__ = [
    "CSS_PATHS",
    "screens",
    "widgets",
]