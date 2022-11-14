def char_indexes(sign):
    dict_of_indexes = {}
    index = 0
    for char in sign:
        if char in dict_of_indexes:
            dict_of_indexes[char].append(index)
        else:
            dict_of_indexes[char] = [index]
        index += 1
    return dict_of_indexes


print(char_indexes('Ala ma kota'))
