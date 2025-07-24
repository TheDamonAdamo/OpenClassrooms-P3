from datetime import datetime


class Tournament:
    """The tournament class holds all information related to a tournament"""

    DATE_FORMAT = "%d-%m-%Y"

    def __init__(self, name, venue, number_of_rounds, current_round, completed, players, finished, rounds):
        if not name:
            raise ValueError("Tournament name is required!")

        self.name = name
        self.venue = venue
        self.number_of_rounds = number_of_rounds
        self.current_round = current_round
        self.completed = completed
        self.players = players
        self.finished = finished
        self.rounds = rounds

        # The class uses a private attribute for the birthdate (datetime format)
       # self._birthdate = None
        # And a public one with a getter/setter for the birthday (str)
        #self.birthday = birthday

    def __str__(self):
        return f"<{self.name}>"

    def __hash__(self):
        """Returns the hash of the object - useful to use the instance as a key in a dictionary or in a set"""
        return hash((self.name, self.venue, self.number_of_rounds, self.current_round, self.completed, self.players, self.finished, self.rounds))

    def __eq__(self, other):
        """Required when __hash__ is defined"""
        if type(other) is not type(self):
            raise TypeError("'=' is not supported with type %s" % type(other))

        return (self.name, self.venue, self.number_of_rounds, self.current_round, self.completed, self.players, self.finished, self.rounds) == (
            other.name,
            other.venue,
            other.number_of_rounds,
            other.current_round,
            other.completed,
            other.players,
            other.finished,
            other.rounds
        )

    @property
    def birthday(self):
        """Property to get the birthday (string) from the birthdate (datetime)"""
        return self.birthdate.strftime(self.DATE_FORMAT)

    @birthday.setter
    def birthday(self, value):
        """Sets the birthdate (datetime) from a string"""
        self.birthdate = datetime.strptime(value, self.DATE_FORMAT)

    def serialize(self):
        """Serialize the instance in a format compatible with JSON"""

        data = {attr: getattr(self, attr) for attr in ("name", "venue", "number_of_rounds", "current_round", "completed", "players", "finished", "rounds")}
        # We make sure to use the str representation of the date
        # datetime is not natively serializable in JSON
        #data["birthday"] = self.birthday
        return data
