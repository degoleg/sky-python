with open('students.txt', encoding="utf-8") as file:
    for student_data in file:

        data = student_data.rstrip('\n').split(":")

        name = data[0]
        language = data[1]

        # name, language = student_data.strip('\n').split(":") можно использовать такой вариант

        print(f"{name} учит язык {language}!")
