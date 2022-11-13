def pattern(number_of_lines):
    string_to_return = ''
    for i in range(number_of_lines):
        if i % 2 == 0:
            string_to_return += '*'
        else:
            string_to_return += '$'
        print(string_to_return)


n = int(input())
pattern(n)
