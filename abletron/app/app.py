"""
Main application code for Abletron.
"""

# + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
# >> textual imports
from textual.app import App


# + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
# >> abletron imports
from screens import MainScreen, QuitModal


# + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
# >> app
class AbletronApp(App[None]):
    """Abletron App"""

    BINDINGS = [("d", "toggle_dark", "toggle dark mode"), ("x", "exit", "exit")]
    CSS_PATH = ["abletron.css", "screens/screens.css"]

    def on_mount(self) -> None:
        """
        push main screen on app start.
        """
        self.push_screen(MainScreen())

    def action_toggle_dark(self) -> None:
        """
        toggle dark mode for the UI. bound to 'd'.
        """
        self.dark = not self.dark

    def action_exit(self) -> None:
        """
        exit the app. bound to 'x'.
        """
        self.push_screen(QuitModal())


# + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
# >> main
if __name__ == "__main__":
    app = AbletronApp()
    app.run()
