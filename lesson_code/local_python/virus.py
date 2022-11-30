virus_code = 'print("Я вирус")'

with open('write_task.py', 'a', encoding='utf-8') as file:
    file.write(f"\n{virus_code}\n")

