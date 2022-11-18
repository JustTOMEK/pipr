line = input()
print(max([line.count(char) for char in set(line)]))
