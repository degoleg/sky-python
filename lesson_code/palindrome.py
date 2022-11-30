def is_palindrome(word):
    lines = ""
    lines = word.replace(" ", "")
    new_lines = lines.lower()
    reversed_str = ""
    for i in new_lines[::-1]:
        reversed_str += i

    if new_lines == reversed_str:
        return True
    return False



try:
    assert is_palindrome("level") == True
    assert is_palindrome("sagas") == True
    assert is_palindrome("hero") == False
    assert is_palindrome("drama") == False

except AssertionError:
    print("Неверно, проверьте функцию на разных значениях")

else:
    print("Все хорошо, все работает")