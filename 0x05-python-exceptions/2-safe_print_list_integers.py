#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        j = 0
        for i in range(x):
            if type(my_list[i]) == int:
                print("{:d}".format(my_list[i]), end="")
                j += 1
            else:
                continue
        print()
        return j
    except ValueError:
        pass
