def create_list_above_average(list):
    average_of_a_list = sum(list)/len(list)
    new_list = []
    for element in list:
        if element >= average_of_a_list:
            new_list.append(element)
    return new_list


print(create_list_above_average([2, -1, 4, -2, 5, 0]))
