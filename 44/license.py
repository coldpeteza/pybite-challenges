# use one or more Standard Library modules
from secrets import choice


def gen_key(parts: int = 4, chars_per_part: int = 8) -> str:
    """
    Generate and return a random license key containing
    upper case characters and digits.

    Example with default "parts" and "chars_per_part"
    being 4 and 8: KI80OMZ7-5OGYC1AC-735LDPT1-4L11XU1U

    If parts = 3 and chars_per_part = 4 a random license
    key would look like this: 54N8-I70K-2JZ7
    """
    letters = [chr(ord('a') + letter) for letter in range(26)]
    numbers = [str(number) for number in range(1, 10)]
    upper_case = [upper.upper() for upper in letters]
    result = ''
    for part in range(parts):
        for char in range(chars_per_part):
            result += choice(numbers+upper_case)
        result += '-'

    # chop off the last '-'
    return result[:len(result)-1]