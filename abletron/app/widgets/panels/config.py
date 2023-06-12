"""
configuration panel widget for Abletron.
"""

# + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
# >> textual imports

from textual.app import ComposeResult
from textual.containers import Container, Vertical
from textual.widgets import (
    Button,
    Label,
    Placeholder,
)


# + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
# >> class definition
class ConfigPanel(Vertical):
    """
    configuration panel widget for Abletron.
    """

    def compose(self) -> ComposeResult:
        """
        compose the config panel.
        """
        # yield Container(
        #     Label("[u]config[/u]"),
        #     id="title",
        # )
        with Container(id="button_grid"):
            yield Button("input paths", id="inputs_btn", classes="button doubled")
            yield Button("output path", id="output_btn", classes="button doubled")
            yield Button(
                "edit categories",
                id="categories_btn",
                classes="button doubled",
                variant="primary",
            )
            yield Button("import", id="import_btn", classes="button io")
            yield Button("export", id="export_btn", classes="button io")
