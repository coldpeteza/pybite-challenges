VOWELS = 'aeiou'
PYTHON = 'python'


def contains_only_vowels(input_str):
    """Receives input string and checks if all chars are
       VOWELS. Match is case insensitive."""
    input_str = input_str.lower()
    count = 0
    for letter in input_str:
        if letter in VOWELS:
            count += 1

    return count == len(input_str)


def contains_any_py_chars(input_str):
    """Receives input string and checks if any of the PYTHON
       chars are in it. Match is case insensitive."""
    input_str = input_str.lower()
    count = 0
    for letter in input_str:
        if letter in PYTHON:
            count += 1

    return count > 0


def contains_digits(input_str):
    """Receives input string and checks if it contains
       one or more digits."""
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    count = 0
    for letter in input_str:
        if letter in digits:
            count += 1

    return count > 0
