def sum_numbers(numbers=None):
    result = 0
    if numbers is None:
        for i in range(1,100):
            result += i
    else:
        for i in numbers:
            result += i
            
    return result
    