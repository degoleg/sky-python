fish = [

{"specie": "Белуга", "water": "fresh"},
{"specie": "Карась", "water": "fresh"},
{"specie": "Красноперка", "water": "fresh"},

{"specie": "Морской окунь", "water": "sea"},
{"specie": "Тунец", "water": "sea"},
{"specie": "Скумбрия", "water": "sea"},

]

sea_water = []
fresh_water = []

for temporary_fish in fish:
    if temporary_fish["water"] == "sea":
        sea_water.append(temporary_fish["specie"])
    else:
        fresh_water.append(temporary_fish["specie"])

new_sea_water = ", ".join(sea_water)

print(f"Морские: {new_sea_water}")

new_fresh_water = ", ".join(fresh_water)

print(f"Пресноводные: {new_fresh_water}")


