"""
main screen for Abletron.
"""

# + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
# >> textual imports

from textual.app import ComposeResult
from textual.screen import Screen
from textual.containers import Horizontal, Vertical
from textual.widgets import (
    Footer,
    Header,
    Placeholder,
)


# + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
# >> abletron imports

from widgets.panels import ConfigPanel, EditorPanel


# + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
# >> class definition
class MainScreen(Screen):
    """
    main screen for Abletron.
    """

    def compose(self) -> ComposeResult:
        yield Header(name="Abletron")
        with Horizontal(id="main"):
            yield ConfigPanel(id="config", classes="panel")
            yield EditorPanel(id="editor", classes="panel")
        yield Footer()
