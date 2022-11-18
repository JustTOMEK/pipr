import math as m


def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, m.ceil(m.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def prime_to_n(n):
    prime_bools = [True]*(n+1)
    for i in range(2, m.ceil(m.sqrt(n)) + 1):
        if prime_bools[i]:
            for j in range(i * 2, n+1, i):
                prime_bools[j] = False
    return [i for i in range(2, n+1) if prime_bools[i]]


def sum_for_list(lst):
    final_array = []
    sqrt_of_max = m.ceil(m.sqrt(max([abs(element) for element in lst])) + 1)
    primes = prime_to_n(max([abs(element) for element in lst]) // 2)
    for prime in primes:
        sum_of_divisible = 0
        counter = 0
        for number in lst:
            if number % prime == 0:
                sum_of_divisible += number
                counter = 1
        if counter == 1:
            final_array.append([prime, sum_of_divisible])
    for number in lst:
        if (abs(number) > sqrt_of_max and is_prime(abs(number)) and
           [abs(number), number] not in final_array):
            final_array.append([abs(number), number])
    final_array.sort(key=lambda x: x[0])
    return final_array
