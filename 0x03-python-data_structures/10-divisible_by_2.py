#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    lst_len = len(my_list)
    nw_lst = []
    for i in range(lst_len):
        if my_list[i] % 2 == 0:
            nw_lst.append(True)
        else:
            nw_lst.append(False)
    return nw_lst

