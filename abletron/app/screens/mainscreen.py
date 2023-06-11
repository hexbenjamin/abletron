"""
main screen for Abletron.
"""

# + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
# >> textual imports

from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import (
    Footer,
    Header,
    # Placeholder,
)


# + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
# >> class definition
class MainScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header(name="Abletron")
        # stuff lol
        yield Footer()
