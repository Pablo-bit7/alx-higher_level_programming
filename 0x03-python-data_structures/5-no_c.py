#!/usr/bin/env python3
def no_c(my_string):
    if my_string[:]:
        new_str = my_string.translate({ord("c"): None})
        sec_str = new_str.translate({ord("C"): None})
        return sec_str
    return my_string

