def char_counter(line):
    for char in set(line):
        print(f'Number of appearences of {char} in input: {line.count(char)}')


line = input()
char_counter(line)
