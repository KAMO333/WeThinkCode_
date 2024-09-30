def smallest(numbers):
    smallest = 0
    for number in numbers:
        if min(numbers) > smallest or min(numbers) < smallest:
            smallest = number
    return smallest