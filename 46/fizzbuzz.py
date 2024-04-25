from typing import Union


def fizzbuzz(num: int) -> Union[str, int]:

    result: str | int = str(num)

    if num % 3 == 0:
        if num % 5 == 0:
            result = "FizzBuzz"
        result = "Fizz"
    elif num % 5 == 0:
        result = "Buzz"
    else:
        result = num

    return result
