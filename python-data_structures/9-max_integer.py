#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:    # if list is empty
        return None

    max_v = my_list[0]  # assume first element is max
    for num in my_list[1:]:
        if num > max_v:
            max_v = num

    return max_v
