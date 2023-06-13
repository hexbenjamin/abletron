"""The main application class."""

from textual import __version__ as textual_version
from textual.app import App

from .. import __version__
# from ..screens import MainScreen


class AbletronApp(App[None]):
    """The main application class."""
    
    TITLE = "Abletron"
    
    def __init__(self):
        """
        Initialize the application.
        """
        
        super().__init__()
    
    def on_mount(self) -> None:
        """Set up the application after initial build."""
        
        pass
        # self.push_screen(MainScreen())


def run() -> None:
    """Run the application."""
    AbletronApp().run()