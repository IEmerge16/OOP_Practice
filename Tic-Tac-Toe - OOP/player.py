class Player:
    number_of_players = 0
    def __init__(self, name: str):
        self.name = name
        Player.number_of_players += 1
        if Player.number_of_players == 1:
            self.mark = "X"
        else:
            self.mark = "O"
        if Player.number_of_players >= 2:
            Player.number_of_players = 0

    def __repr__(self):
        return f"{self.name} using {self.mark}"