"""
Name: Lucas Vanzelli
Pledge: I pledge my honor that I have abided by the Stevens Honor System
Date: 9/17/2023
"""
from functools import reduce

##This function returns the product of x and y
def mult(x,y):
    return x * y

#This function returns n!
def factorial(n):
    return reduce(mult, range(1,n+1))

##This function returns the sum of x + y
def add(x,y):
    return x + y

##This function returns the mean of the numbers in the list L
def mean(L):
    listMean = (reduce(add, L)) / len(L)
    return listMean

