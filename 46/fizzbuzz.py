from typing import Union


def fizzbuzz(num: int) -> Union[str, int]:

    result: str | int = str(num)

    if num % 3 == 0:
        if num % 5 == 0:
            result = "Fizz Buzz"
        else:
            result = "Fizz"
    elif num % 5 == 0:
        result = "Buzz"
    else:
        result = num

    return result

# if __name__ == '__main__':
#     for i in range(1, 17):
#         print(fizzbuzz(i))