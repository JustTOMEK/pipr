deliveries = [{'mass': 20, 'name': 'cebula', 'weekday': 'poniedziałek'},
              {'mass': 30, 'name': 'czosnek', 'weekday': 'poniedziałek'},
              {'mass': 40, 'name': 'marchew', 'weekday': 'poniedziałek'},
              {'mass': 50, 'name': 'ogórek', 'weekday': 'poniedziałek'},
              {'mass': 60, 'name': 'cebula', 'weekday': 'poniedziałek'},
              {'mass': 70, 'name': 'pietruszka', 'weekday': 'poniedziałek'},
              {'mass': 80, 'name': 'cebula', 'weekday': 'poniedziałek'},
              {'mass': 90, 'name': 'ogórek', 'weekday': 'poniedziałek'},
              {'mass': 100, 'name': 'czosnek', 'weekday': 'poniedziałek'},
              {'mass': 110, 'name': 'ogórek', 'weekday': 'poniedziałek'},
              {'mass': 120, 'name': 'cebula', 'weekday': 'poniedziałek'},
              {'mass': 130, 'name': 'cukinia', 'weekday': 'poniedziałek'}]


mass = 0
for dict in deliveries:
    if dict['name'] == 'ogórek':
        mass += dict['mass']
print(mass)
