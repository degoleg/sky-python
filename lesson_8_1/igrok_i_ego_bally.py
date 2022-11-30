class Player:

  def __init__(self, name, score):
    self.name = name
    self.score = 0

  def get_score(self):
    return self.score

  def set_score(self, score):
    self.score = score


player_1 = Player("Алиса", 0)


# Не удаляйте этот код, он нужен для проверки

print(player_1.name, player_1.get_score())
player_1.set_score(200)
print(player_1.name, player_1.get_score())
player_1.set_score(500)
print(player_1.name, player_1.get_score())