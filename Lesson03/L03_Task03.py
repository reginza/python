def my_func(args_numbers):
    min_number = min(args_numbers)
    args_numbers.remove(min_number)
    return sum(args_numbers)


numbers = [40, 80, 90]
print(my_func(numbers))
