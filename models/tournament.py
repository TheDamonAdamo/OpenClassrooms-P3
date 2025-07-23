import json

from .tournament_info import Tournament


class ChessTournament:
    """
    A local chess tournament

    Data is loaded from a JSON file (provided as argument).
    The class creates Tournament instances based on JSON data.
    """

    def __init__(self, filepath=None, name=None):
        """The constructor works in two ways:
        - if the filepath is provided, it loads data from JSON
        - if it is not but a name is provided, it creates a new tournament (and a new JSON file)
        """

        self.name = name
        self.filepath = filepath
        self.tournaments = []

        if filepath and not name:
            # Load data from the JSON file
            with open(filepath) as fp:
                data = json.load(fp)
                self.name = data["name"]
                self.tournaments = [
                    Tournament(**tournament_dict) for tournament_dict in data["tournaments"]
                ]
        elif not filepath:
            # We did not have a file, so we are going to create it by running the save method
            self.save()

    def save(self):
        """Serializes the tournaments and saves the tournament info to the JSON file"""

        with open(self.filepath, "w") as fp:
            json.dump(
                {"name": self.name, "tournaments": [p.serialize() for p in self.tournaments]},
                fp,
            )

    def create_tournaments(self, **kwargs):
        """Utility method to create a new tournament instance and add it to the club"""

        tournament = Tournament(**kwargs)
        self.tournaments.append(tournament)
        self.save()
        return tournament

    def update_tournament(self, tournament, **kwargs):
        """Utility method to update a tournament instance based on arguments provided"""

        if tournament not in self.tournaments:
            raise RuntimeError(f"Tournament {tournament} not in club {self.name}!")

        for key, value in kwargs.items():
            setattr(tournament, key, value)

        self.save()
        return tournament
