def earnings(first, second):
    new_dict = {}
    for person in first:
        new_dict[person] = first[person][1] * first[person][0]
        new_dict[person] += second[person][1] * second[person][0]
    return new_dict


first_project = {
    'Anna Nowak': (20, 52.5),
    'Jan Kowalski': (10, 24.5),
    'Jan Śnieg': (15, 32.25),
    'Karolina Windsor': (40, 30.5)
}
second_project = {
    'Anna Nowak': (10, 44.0),
    'Jan Kowalski': (25, 20.0),
    'Jan Śnieg': (15, 32.25),
    'Karolina Windsor': (10, 22.75)
}
print(earnings(first_project, second_project))
