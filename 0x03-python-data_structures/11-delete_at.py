#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    lst_len = len(my_list)
    if idx > lst_len - 1:
        return my_list
    elif idx < 0:
        return my_list
    del my_list[idx]
    return my_list

