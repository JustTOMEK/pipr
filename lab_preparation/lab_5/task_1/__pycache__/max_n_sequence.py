def max_n_sequence(sequence, length):
    if length > len(sequence):
        return None
    sums = []  # stores sum of each sequence
    index = 0
    for index in range(len(sequence) - length + 1):
        sums.append(sum(sequence[index:index + length]))
    return max(sums)


print(max_n_sequence([1, 2, 3, 1, 3, 4, 5, 6, 1, 4], 2))
