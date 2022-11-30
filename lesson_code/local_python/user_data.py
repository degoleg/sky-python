filename = "user_data.txt"
f = open(filename, "r")
name = f.readline().replace("\n", "")
surname = f.readline().replace("\n", "")
email = f.readline().replace("\n", "")
phone = f.readline().replace("\n", "")


print(f"{name} {surname} – это вы. Ваша почта {email}, ваш телефон {phone}")

