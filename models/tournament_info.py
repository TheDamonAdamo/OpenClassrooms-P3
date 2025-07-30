#from datetime import datetime

#from TestFiles.jsontest2 import dates_from


class Tournament:
    """The tournament class holds all information related to a tournament"""

    DATE_FORMAT = "%d-%m-%Y"

    def __init__(self, name, venue, dates, number_of_rounds, current_round, completed, players, rounds):
        if not name:
            raise ValueError("Tournament name is required!")

        self.name = name
        self.venue = venue
        self.dates_from = dates[0]
        self.dates_to = dates[1]
        self.number_of_rounds = number_of_rounds
        self.current_round = current_round
        self.completed = completed
        self.players = players
        self.rounds = rounds

        # The class uses a private attribute for the birthdate (datetime format)
        self._dates_from_date = None
        self._dates_to_date = None
        # And a public one with a getter/setter for the birthday (str)
        self.dates_from = dates_from
        #self.dates_to = dates_to

    def __str__(self):
        return f"<{self.name}>"

    def __hash__(self):
        """Returns the hash of the object - useful to use the instance as a key in a dictionary or in a set"""
        return hash((self.name, self.venue, self.dates_from, self.number_of_rounds, self.current_round, self.completed, self.players, self.rounds))

    def __eq__(self, other):
        """Required when __hash__ is defined"""
        if type(other) is not type(self):
            raise TypeError("'=' is not supported with type %s" % type(other))

        return (self.name, self.venue, self.number_of_rounds, self.current_round, self.completed, self.players,  self.rounds) == (
            other.name,
            other.venue,
            other.number_of_rounds,
            other.current_round,
            other.completed,
            other.players,
            other.rounds
        )


        return data
