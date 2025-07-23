from commands import TournamentListCmd
from screens import TournamentCreate, TournamentView, TournamentMenu, TournamentEdit


class App:
    """The main controller for the tournament management program"""

    SCREENS = {
        "tourny-menu": TournamentMenu,
        "tournament-view": TournamentView,
        "tournament-edit": TournamentEdit,
        "tournament-create": TournamentCreate,
        "exit": False,
    }

    def __init__(self):
        # We start with the list of clubs (= main menu)
        command = TournamentListCmd()
        self.context = command()

    def run(self):
        while self.context.run:
            # Get the screen class from the mapping
            screen = self.SCREENS[self.context.screen]
            try:
                # Run the screen and get the command
                command = screen(**self.context.kwargs).run()
                # Run the command and get a context back
                self.context = command()
            except KeyboardInterrupt:
                # Ctrl-C
                print("Bye!")
                self.context.run = False


if __name__ == "__main__":
    app = App()
    app.run()
