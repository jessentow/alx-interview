#!/usr/bin/python3
"""
    0-pascal_triangle.py: pascal_triangle()
"""


def pascal_triangle(n):
    """
        returns a lists of integers
        Args:
            n (int): number of lists and digits
        Returns: list of lists
    """
    row_T = [1]
    G_1 = [0]
    Pascal_T = []

    if n <= 0:
        return Pascal_T

    for i in range(n):
        Pascal_T.append(row_T)
        row_T = [l+r for l, r in zip(row_T + G_1, G_1 + row_T)]
    return Pascal_T
