from commands import TournamentCreateCmd

from ..base_screen import BaseScreen


class TournamentCreate(BaseScreen):
    """Screen displayed when creating a club"""

    display = "## Create tournament"

    def get_command(self):
        print("Type in the name of the club")
        name = self.input_string()

        return TournamentCreateCmd(name)
