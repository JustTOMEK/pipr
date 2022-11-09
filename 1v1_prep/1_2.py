def most_appereances(string):
    most = []
    apperances = []
    for char in set(string):
        if char == ' ':
            continue
        else:
            apperances.append([char, string.count(char)])
    maks = max(apperances, key=lambda x: x[1])
    for element in apperances:
        if element[1] == maks[1]:
            most.append(element[0])
    return most


string = "Dawno nie byłem w szkolell"
for char in most_appereances(string):
    print(char)
