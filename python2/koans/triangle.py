#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.


# triangle(a, b, c) analyzes the lengths of the sides of a triangle
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
def triangle(a, b, c):
    # DELETE 'PASS' AND WRITE THIS CODE
    if a == b:
        return b == c and 'equilateral' or 'isosceles'
        #if b == c:
            #return 'equilateral'
        #else:
            #return 'isosceles'
    else:
        if a == c or b == c:
            return 'isosceles'
        else:
            return 'scalene'


# Error class used in part 2.  No need to change this code.
class TriangleError(StandardError):
    pass

if __name__ == '__main__':
    print triangle(3, 4, 4)
    print triangle(4, 4, 4)
