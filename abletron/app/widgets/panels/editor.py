"""
editor panel widget for Abletron.
"""

# + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
# >> textual imports

from textual.app import ComposeResult
from textual.containers import Container, Vertical
from textual.widgets import (
    Placeholder,
)


# + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
# >> class definition
class EditorPanel(Vertical):
    """
    editor panel widget for Abletron.
    """

    def compose(self) -> ComposeResult:
        """
        compose the editor panel.
        """
        yield Container(Placeholder("#input_fp / .fp"), id="input_fp", classes="fp")
        yield Container(Placeholder("#button_row"), id="button_row")
        yield Container(Placeholder("#output_fp / .fp"), id="output_fp", classes="fp")
