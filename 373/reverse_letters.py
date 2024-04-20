from collections import deque


def reverse_letters(string: str) -> str:
    """Reverse letters in a string but keep the order of the non-letters the same"""
    stack = deque()
    result = ['' for _ in range(len(string))]
    print(len(result))
    for position, letter in enumerate(string):
        if letter.isalpha():
            stack.append(letter)
        else:
            result[position] = letter

    counter = 0
    while stack:
        if not result[counter]:
            result[counter] = stack.pop()
        counter += 1

    return "".join(result)



if __name__ == "__main__":
    print(reverse_letters('Hello 2 World'))