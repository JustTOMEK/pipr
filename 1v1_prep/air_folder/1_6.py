def max_people_on_1_place(log):
    number_of_people = [0] * len(log)
    max_people = 0
    for action in log:
        if action[0] == 'enter':
            number_of_people[action[1] - 1] += 1
        else:
            number_of_people[action[1] - 1] -= 1
        if max(number_of_people) > max_people:
            max_people = max(number_of_people)
    return max_people


log = [('enter', 1),
       ('enter', 1),
       ('enter', 2),
       ('enter', 3),
       ('enter', 2),
       ('enter', 2),
       ('enter', 2),
       ('exit', 3),
       ('exit', 4),
       ('exit', 1),
       ('exit', 2),
       ('exit', 1),
       ('exit', 2),
       ('exit', 2)]

print(max_people_on_1_place(log))
