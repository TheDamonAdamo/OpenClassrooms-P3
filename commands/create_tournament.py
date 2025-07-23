from commands.context import Context
from models import ClubManager

from .base import BaseCommand


class TournamentCreateCmd(BaseCommand):
    """Command to create a club"""

    def __init__(self, name):
        self.name = name

    def execute(self):
        """Uses a TournamentManager instance to create the club and add it to the list of torunaments"""
        tm = TournamentManager()
        tournament = tm.create(self.name)
        return Context("tournament-view", tournament=tournament)