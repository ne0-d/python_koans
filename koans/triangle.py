#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(side1, side2, side3):
    if side1 <= 0 or side2 <= 0 or side3 <= 0 or (side1 + side2 <= side3) or (side1 + side3 <= side2) or (side2 + side3 <= side1):
        raise TriangleError

    if side1 == side2 == side3:
        return 'equilateral'

    if side1 == side2 or side1 == side3 or side2 == side3:
        return 'isosceles'

    return 'scalene'

# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass


