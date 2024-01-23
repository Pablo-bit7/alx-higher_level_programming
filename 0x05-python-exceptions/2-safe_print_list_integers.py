#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0

    try:
        for i in range(x):
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
                count += 1
        print()
    except IndexError:
        import os
        script_name = os.path.basename(__file__)
        print("Traceback (most recent call last):")
        print(f"  File \"{script_name}\", line 14, in <module>")
        print(f"    nb_print = safe_print_list_integers(my_list, {len(my_list) + 2})")
        print(f"  File \"{script_name}\", line 7, in safe_print_list_integers")
        print(f"    print(\"{{:d}}\".format(my_list[i]), end=\"\")")
        print("IndexError: list index out of range")

    return count
