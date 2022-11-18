def average(numbers):
    return sum(numbers) / len(numbers)


def mod_greater_than_first_half(numbers):
    mod_1 = [numbers[i] for i in range(len(numbers)) if i % 3 == 1]
    first_half = numbers[:len(numbers) // 2]
    return average(mod_1) > average(first_half)


numbers = [1, 2, 3, 4, 10, 2, 3, 4, 5, 1, 1, 1]
print(mod_greater_than_first_half(numbers))
