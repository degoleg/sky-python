order = [
 {"skolko": 5.0, "poroda": "тунец", "sred_razmer": 300},
 {"skolko": 15.0, "poroda": "окунь", "sred_razmer": 250},
 {"skolko": 20.0, "poroda": "щука", "sred_razmer": 460},
]
order_converted = []


for orde in order:
    order_position = {
    "count": int(orde["skolko"]),
    "specie": orde["poroda"].title(),
    "avg_size": orde["sred_razmer"] // 10
    }

    order_converted.append(order_position)


#Не удаляйте текст ниже, он нужен для проверки

for item in order_converted:
  for key, value in item.items():
      print(key, value)