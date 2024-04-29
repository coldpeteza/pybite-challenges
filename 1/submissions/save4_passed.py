def sum_numbers(numbers=None):
    result = 0
    if numbers is None:
        result = sum(range(1,101))
    else:
        for i in numbers:
            result += i
            
    return result
    