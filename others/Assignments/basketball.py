from players import players

class Player:
    # team=[]
    # Challenge 1: Update the Constructor
    def __init__(self, data):
        self.name = data["name"]
        self.age = data["age"]
        self.position = data["position"]
        self.team = data["team"]
        # Player.team.append(self)

    # # NINJA BONUS: Add a get_team(cls, team_list) @class method
    # @classmethod
    # def get_team(cls, team_list):
    #     for player in team_list:
    #         cls.team.append(player)
    #     return cls.team

    # * NINJA BONUS class mehotd
    @classmethod
    def add_players(cls, data):
        player_objects = []
        for dict in data:
            player_objects.append(cls(dict))
        return player_objects


    def __repr__(self):
        return "Player: {}, {} y/o, pos: {}, team: {}\n".format(self.name, self.age, self.position, self.team)
    
# Create your Player instances here!
# player_jason = ???

# Challenge 2: Create instances using individual player dictionaries.
kevin = Player(players[0])
jason = Player(players[1])
kyrie = Player(players[2])

# Challenge 3: Make a list of Player instances from a list of dictionaries
new_team = []
for player_dict in players:
    new_team.append(Player(player_dict))


print(kevin)
print(new_team)
