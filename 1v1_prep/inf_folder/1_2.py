def most_appeareances(string):
    most = []
    appereances = []
    for char in set(string):
        if char != ' ':
            appereances.append([char, string.count(char)])
    maks = max(appereances, key=lambda x: x[1])[1]
    for element in appereances:
        if element[1] == maks:
            most.append(element[0])
    return most


string = "Dawno nie byłem w szkolell"
for element in most_appeareances(string):
    print(element)
