def sum_numbers(numbers=None):
    result = 0
    if numbers is None:
        for i in range(100):
            result += i
    else:
        for i in numbers:
            result += i
            
    return result
    
print(sum_numbers())
print(sum_numbers([1,2]))
print(sum_numbers([]))
