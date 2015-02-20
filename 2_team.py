class Player:

  def __init__(self, name, jersey_number):
    self.name = name
    self.number = jersey_number



class Team:

  def __init__(self, team_name):
    self.name = team_name
    self.players = []

  def add_player(self, player):
    self.players.append(player)

  def display(self):
    print(self.name)
    print("-------------------------")
    for player in self.players:
      print("{0:<4} {1}".format(player.number, player.name))


player1 = Player("Jeff", 21)

player2 = Player("Hannah", 44)
player3 = Player("Nick", 16)
player4 = Player("Philip", 16)
player5 = Player("Christoper", 22)
player6 = Player("David", 10)

home_team = Team("Chicago")
away_team = Team("New York")

home_team.add_player(player1)
home_team.add_player(player2)
player1.name = "WazzzupJeff"
home_team.display()

away_team.add_player(player3)
away_team.add_player(player4)
away_team.display()






