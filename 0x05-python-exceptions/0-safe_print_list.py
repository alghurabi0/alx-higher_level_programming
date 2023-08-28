#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        d = 0
        for el in my_list:
            d += 1
        if d < x:
            raise IndexError
        else:
            d = 0
            for i in range(x):
                print(my_list[i], end="")
                d = d + 1
            print()
        return d
    except IndexError:
        j = 0
        for num in my_list:
            print(num, end="")
            j = j + 1
        print()
        return j
