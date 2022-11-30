class Bottle:
    def __init__(self, color, contains):
        self.color = color
        self.contains = contains

    def get_content(self):
        return float(self.contains)

    def fill(self, volume):
        self.contains += volume


bottle_1 = Bottle("Красная", 0)
bottle_2 = Bottle("Синяя", 0)

# Не удаляйте этот код, он нужен для проверки

print(bottle_1.color, bottle_1.get_content())
bottle_1.fill(100)
print(bottle_1.color, bottle_1.get_content())

print(bottle_2.color, bottle_2.get_content())
bottle_2.fill(500)
print(bottle_2.color, bottle_2.get_content())