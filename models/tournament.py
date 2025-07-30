import json

from .tournament_info import Tournament


class ChessTournament:
    """
    Manages a single chess tournament, loading and saving its data.
    This class now directly represents the attributes of one tournament.
    """

    def __init__(self, filepath=None, name=None): # 'name' argument might become redundant if always loaded from file
        self.filepath = filepath
        self.tournament_data = {} # This will store the dictionary loaded from JSON

        # Initialize attributes for the tournament directly
        self.name = name
        self.dates = {}
        self.venue = None
        self.number_of_rounds = 0
        self.current_round = None
        self.completed = False
        self.players = []
        self.finished = False
        self.rounds = []

        if filepath:
            try:
                with open(filepath, 'r') as fp:
                    data = json.load(fp)

                    # Now, instead of creating a list of Tournament objects,
                    # you populate the attributes of THIS ChessTournament instance
                    # directly from the loaded 'data' dictionary.
                    # Or, if you want to wrap it in a 'Tournament' object, do it once.

                    # Option A: Directly populate this ChessTournament's attributes
                    self.name = data.get("name")
                    self.dates = data.get("dates", {})
                    self.venue = data.get("venue")
                    self.number_of_rounds = data.get("number_of_rounds", 0)
                    self.current_round = data.get("current_round")
                    self.completed = data.get("completed", False)
                    self.players = data.get("players", [])
                    self.finished = data.get("finished", False)
                    self.rounds = data.get("rounds", [])

                    # If you still want an instance of `models.tournament_info.Tournament`
                    # as an internal object, you'd create one instance like this:
                    self._tournament_info_instance = Tournament(**data) # Pass the whole dict to your Tournament class

            except FileNotFoundError:
                print(f"Warning: Tournament file not found at {filepath}. Initializing with default values.")
                # Keep default initialized attributes
                self.name = name if name else "New Tournament" # Or whatever default name
            except json.JSONDecodeError:
                print(f"Error: Could not decode JSON from {filepath}. Check file format.")
                # Keep default initialized attributes
            except Exception as e:
                print(f"An unexpected error occurred while loading {filepath}: {e}")
                # Keep default initialized attributes

        elif not filepath and name:
            # This block would be for creating a brand new tournament when no file exists
            # and a name is provided.
            self.name = name
            # Other attributes already initialized to defaults above
            self.save() # Save the newly created (empty) tournament data
        else:
            # Scenario: no filepath and no name given - initialize empty tournament
            print("No filepath or name provided. Initializing an empty tournament.")
            # Attributes are already at their default empty values

    def save(self):
        """Saves the current tournament's data to the JSON file."""
        if not self.filepath:
            raise ValueError("Cannot save: No filepath provided for this tournament instance.")

        # If you are directly managing attributes:
        data_to_save = {
            "name": self.name,
            "dates": self.dates,
            "venue": self.venue,
            "number_of_rounds": self.number_of_rounds,
            "current_round": self.current_round,
            "completed": self.completed,
            "players": self.players,
            "finished": self.finished,
            "rounds": self.rounds
        }

        # If you're managing an internal _tournament_info_instance and it has a serialize method:
        # if hasattr(self, '_tournament_info_instance') and self._tournament_info_instance:
        #     data_to_save = self._tournament_info_instance.serialize()
        # else:
        #     # Fallback if no instance or not serialized
        #     # You'd need to convert the current attributes to a dict
        #     data_to_save = {
        #         "name": self.name,
        #         "dates": self.dates,
        #         # ... other attributes
        #     }


        with open(self.filepath, "w") as fp:
            json.dump(data_to_save, fp, indent=4) # Use indent for pretty printing JSON

    # You would then add methods to interact with this single tournament's data
    # For example:
    def add_player(self, player_id):
        if player_id not in self.players:
            self.players.append(player_id)
            self.save()
            print(f"Player {player_id} added to {self.name}.")
        else:
            print(f"Player {player_id} already in {self.name}.")

    def start_next_round(self):
        # Logic to generate pairings for the next round
        pass

    # You'd also need a way to create a new tournament file from manage_tournament.py
    # This might involve passing a new filepath and a new name to the ChessTournament constructor.


    def create_tournaments(self, **kwargs):
        """Utility method to create a new tournament instance and add it to the club"""

        tournament = Tournament(**kwargs)
        self.tournament.append(tournament)
        self.save()
        return tournament

    def update_tournament(self, tournament, **kwargs):
        """Utility method to update a tournament instance based on arguments provided"""

        if tournament not in self.tournament:
            raise RuntimeError(f"Tournament {tournament} not in club {self.name}!")

        for key, value in kwargs.items():
            setattr(tournament, key, value)

        self.save()
        return tournament
