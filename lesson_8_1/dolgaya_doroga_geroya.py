class Hero:

  def go_right(self, met):
    print(f"Я иду {met} метров направо")

  def go_left(self, met):
    print(f"Я иду {met} метров налево")

  def observe(self):
    print("Я осматриваюсь")


hero = Hero()

meters = hero.go_right(50)
meters = hero.go_left(30)
hero.observe()