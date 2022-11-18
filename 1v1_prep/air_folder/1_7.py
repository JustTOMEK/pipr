def letters_in_both(first_line, second_line):
    for char in set(first_line):
        if char in second_line and char.isalpha():
            print(char)


first_line = input()
second_line = input()
letters_in_both(first_line, second_line)
