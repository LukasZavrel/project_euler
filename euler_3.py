def is_palindrome(number):
    string = str(number)
    result = True
    for i in range(len(string) // 2):
        if string[i] != string[-i - 1]:
            result = False
    return result


max_number = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        number = i * j
        if is_palindrome(number):
            if max_number < number:
                max_number = number
print(max_number)
