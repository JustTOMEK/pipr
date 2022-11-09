def change_chars(line, to_remove):
    new_line = ''
    for char in line:
        if char in to_remove:
            new_line += ('*')
        else:
            new_line += (char)
    return new_line


print(change_chars('Jacek ma kota', ['a', 'c', 'k']))
