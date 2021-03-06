#!/usr/bin/python3
"""Module 12-pascal_triangle.
Returns a list of lists of integers
representing the Pascal’s triangle of n.
"""


def pascal_triangle(n):
    """Returns the pascal triangle of n.
    Args:
        - n: size of the triangle (rows)
    Returns: a list of list of integers
    """

    if n <= 0:
        return []
    triangles = [[1]]

    while len(triangles) != n:
        tri = triangles[-1]
        lis = [1]
        for i in range(len(tri) - 1):
            lis.append(tri[i] + tri[i + 1])
        lis.append(1)
        triangles.append(lis)
    return triangles
