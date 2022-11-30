from validators.validate_pin import validate_pin
from validators.validate_card import validate_card

print("Введите ваш номер карты")
card_number = input()

print("Введите ваш ПИН-код")
card_pin = input()

result_card_number = validate_card(card_number)

if result_card_number is True:
    print("Номер карты допустимый")
else:
    print("Номер карты недопустимый")

result_card_pin = validate_pin(card_pin)

if result_card_pin is True:
    print("ПИН-код допустимый")
else:
    print("ПИН-код недопустимый")

