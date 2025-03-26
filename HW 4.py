'''p
Created On 10/20/23
@Author: Lucas Vanzelli
I pledge my honor that I have abided by the Stevens Honor System.
CS115 - HW 4
'''

def calcMiddle(x):
    '''
    This function takes a list x, which represents the values
    inbetween the 1's of Pascal's tria
    '''
    if len(x) == 1:
        return []
    else:
        return [x[0] + x[1]] + calcMiddle(x[1:])


def pascal_row(x):
    if x == 0:
        return [1]
    elif x == 1:
        return [1,1]
    else:
        return [1] + calcMiddle(pascal_row(x-1)) + [1]

def pascal_triangle(n):
    if n == 0:
        return [[1]]
    else:
        return pascal_triangle(n-1) + [pascal_row(n)]

def test_pascal_row():
    assert pascal_row(0) == [1]
    assert pascal_row(1) == [1, 1]
    assert pascal_row(2) == [1, 2, 1]
    assert pascal_row(3) == [1, 3, 3, 1]

def test_pascal_triangle():
    assert pascal_triangle(0) == [[1]]
    assert pascal_triangle(1) == [[1], [1, 1]]
    assert pascal_triangle(2) == [[1], [1, 1], [1, 2, 1]]
    assert pascal_triangle(3) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]


