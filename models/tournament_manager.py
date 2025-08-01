import json
from pathlib import Path

from .tournament import ChessTournament


class TournamentManager:
    def __init__(self, data_folder="data/tournaments"):
        datadir = Path(data_folder)
        self.data_folder = datadir
        self.tournaments = []
        for filepath in datadir.iterdir():
            if filepath.is_file() and filepath.suffix == ".json":
                try:
                    self.tournaments.append(ChessTournament(filepath))
                except json.JSONDecodeError:
                    print(filepath, "is invalid JSON file.")

    def create(self, name):
        filepath = self.data_folder / (name.replace(" ", "") + ".json")
        tournament = ChessTournament(name=name, filepath=filepath)
        tournament.save()

        self.tournaments.append(tournament)
        return tournament
