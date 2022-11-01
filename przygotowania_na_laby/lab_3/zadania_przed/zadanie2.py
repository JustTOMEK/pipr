def every_3rd_element_from_the_list_backwards(lista):
    nowa_lista = []
    for i in range(1, len(lista)):
        if (i - 1) % 3 == 0:
            nowa_lista.append(lista[-1*(i+1)])
    return nowa_lista


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(every_3rd_element_from_the_list_backwards(lista))
