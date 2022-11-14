def odd_greater_than_3(numbers):
    sum_of_odd = 0
    sum_off_3 = 0
    for index in range(len(numbers)):
        if index % 2 == 1:
            sum_of_odd += numbers[index]
        if (index) % 3 == 0:
            sum_off_3 += numbers[index]
    return sum_of_odd > sum_off_3


lista = [1, 1, 3, 1, 9, 1, 1, ]
print(odd_greater_than_3(lista))
