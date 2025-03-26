############################################################
# Name: Lucas Vanzelli
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# CS115 Lab 1
#  
############################################################

import math
from functools import reduce

##This function returns the inverse of x
def inverse(x):
    return float(1/x)

##This function finds the sum of the two parameters
def add(x, y):
    return x + y

##This function will find the sum of e in the first n terms of the sequence
def e(n):
    myList = list(range(n+1))
    myList = list(map(math.factorial,myList))
    myList = list(map(inverse,myList))
    return (reduce(add, myList))
    


