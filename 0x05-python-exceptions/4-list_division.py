#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    try:
        for i in range(list_length):
            if my_list_1[i] == 0 or my_list_2[i] == 0:
                raise ZeroDivisionError
            elif (type(my_list_1[i]) == int or type(my_list_1[i]) == float) and (type(my_list_2[i]) == int or type(my_list_2[i] == float)):
                a = my_list_1[i] / my_list_2[i]
                new_list.append(a)
            else:
                raise TypeError
    except ZeroDivisionError:
        print("division by 0")
        new_list.append(0)
        continue
    except TypeError:
        print("wrong type")
        new_list.append(0)
    except IndexError:
        print("out of range")
        new_list.append(0)
    finally:
        return new_list
