employees = {
"Киселёв": {"f": "Киселёв", "i": "Всеволод", "o": "Эдуардович", "pass": "342 020", "birthday": "14 ноября 2001 года", "phone": "+7 (908) 161-64-28", "position": "главный инженер"},
"Довлатова": {"f": "Довлатова", "i": "Эмилия", "o": "Ефимовна", "pass": "342 000", "birthday": "18 мая 2001 года", "phone": "+7 (924) 588-50-15", "position": "технолог"},
"Аверин": {"f": "Аверин", "i": "Мартын", "o": "Егорович", "pass": "217 340", "birthday": "12 февраля 1981 года", "phone": "+7 (933) 768-22-15", "position": "технолог"},
"Князева": {"f": "Князева", "i": "Августа", "o": "Егоровна", "pass": "320 021", "birthday": "2 июля 1984 года", "phone": "+7 (965) 886-27-01", "position": "расфасовщик"},
"Шанская": {"f": "Шанская", "i": "Аграфена", "o": "Семёновна", "pass": "116 404", "birthday": "7 июля 1982 года", "phone": "+7 (954) 940-47-96", "position": "психолог для рыб"},
}
# Не удаляйте код ниже, он важен для проверки!

for employee in employees.values():
  for key, value in employee.items():
      print(key, value)
  print("-")