"""
Write two conversion routines. The first routine convests a string to a signed integer.
You may assume that the string contains only digits and the minus character ('-'),
that it is properly formatted integer number, and that the number is within the range
of an int type. The second routine conversts a signed integer stored as an int back
to string.
"""

def from_string_to_int(number):
    """Function to convert a string to an integer"""
    result = 0

    for index, digit in enumerate(reversed(number)):
        if digit == '-':
            result *= -1
        else:
            result += pow(10, index) * (ord(digit) - ord('0'))

    return result

def from_int_to_string(number):
    """Function to convert an integer to its string representation"""
    result = ""
    numbers = []

    if number < 0:
        result = "-"
        number *= -1

    while True:
        numbers.append(chr(number % 10 + ord('0')))
        number //= 10
        if number == 0:
            break

    numbers = reversed(numbers)
    for char in numbers:
        result += char

    return result

if __name__ == "__main__":
    print from_string_to_int("1")
    print from_int_to_string(-1)
