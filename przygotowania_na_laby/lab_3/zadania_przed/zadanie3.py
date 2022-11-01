def fibonnaci_n_element(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonnaci_n_element(n-1) + fibonnaci_n_element(n-2)


print(fibonnaci_n_element(5))
