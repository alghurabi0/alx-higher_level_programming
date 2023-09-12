#!/usr/bin/python3
""" Returns a list of lists of ints for pascal tiangle. """


def pascal_triangle(n):
    """ Returns a list of lists of ints. """
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [[1], [1, 1]]
    else:
        res = [[1], [1, 1]]
        while len(res) < n:
            idx = len(res) - 1
            next_list = [1]
            prev = res[idx]
            for i in range(1, len(res)):
                next_list.append(prev[i - 1] + prev[i])

            next_list.append(1)
            prev = next_list
            res.append(next_list)

    return res
