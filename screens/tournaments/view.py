from commands import TournamentListCmd, NoopCmd

from ..base_screen import BaseScreen


class TournamentView(BaseScreen):
    """Screen displayed when viewing a tournament"""

    def __init__(self, tournament):
        self.tournament = tournament

    def display(self):
        """Displays the tournament name and a list of players in the tournament (with numbers)"""
        print("##", self.tournament.name)
        for idx, p in enumerate(self.tournament.players, 1):
            print(idx, p.name, p.email)

    def get_command(self):
        """Gets the command for this screen"""
        while True:
            print("Select a player to view/edit it, or 'C' to create a new player.")
            print("Type 'B' to go back to main menu.")
            value = self.input_string()
            if value.upper() == "B":
                return tournamentListCmd()
            elif value.upper() == "C":
                return NoopCmd("player-create", tournament=self.tournament)
            elif value.isdigit():
                value = int(value)
                return NoopCmd(
                    "player-view", tournament=self.tournament, player=self.tournament.players[value - 1]
                )
