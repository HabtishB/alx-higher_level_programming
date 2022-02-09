#!/usr/bin/python3
""" pascal triangle function """


def pascal_triangle(n):
    """ returns a list of lists"""

    if type(n) != int:
        raise TypeError("ints only please")
    if n <= 0:
        return []

    pascal_triangle = [[1]]
    for i in range(n - 1):
        new_list = []
        a = 0
        for j in pascal_triangle[i]:
            b = j
            new_list.append(a + b)
            a = b
        new_list.append(b)
        pascal_triangle.append(new_list)
    return pascal_triangle
