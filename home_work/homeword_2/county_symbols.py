def count_symbols(list_of_symbols):
    number_of_appeareances = {}
    all_symbols = []
    for list in list_of_symbols:
        all_symbols.extend(list)
    for letter in set(all_symbols):
        number_of_appeareances[letter] = all_symbols.count(letter)
    return number_of_appeareances

# data in [['a', 'b', 'c'], ['d', 'b'], ['z']]
