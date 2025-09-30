#!/usr/bin/python3
"""
Module 12-pascal_triangle
Generates Pascal's triangle of size n.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the Pascal's triangle of n.

    Args:
        n (int): The number of rows of the triangle.

    Returns:
        list: A list of lists of integers.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # first row

    for i in range(1, n):
        prev_row = triangle[i - 1]
        row = [1]  # first element is always 1

        # Each inner element is the sum of the two elements above it
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1)  # last element is always 1
        triangle.append(row)

    return triangle
