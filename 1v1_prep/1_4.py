def every_k_k_times(numbers):
    new_list = []
    for number in numbers:
        new_list.extend([number]*number)
    return new_list


numbers = [3, 2, 0, 1]
print(every_k_k_times(numbers))
