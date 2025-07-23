from commands.context import Context

from .base import BaseCommand


class TournamentUpdateCmd(BaseCommand):
    """Command to update a player"""

    def __init__(self, club, player, **data):
        self.tournament = tournament
        self.player = player
        self.data = data

    def execute(self):
        """The command uses the update_player method from the Club model"""
        if self.player:
            player = self.tournament.update_player(self.player, **self.data)
        else:
            player = self.tournament.create_player(**self.data)

        return Context("player-view", tournament=self.tournament, player=player)
