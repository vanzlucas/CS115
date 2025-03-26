'''
Created on 10/19/23
@author: Lucas Vanzelli
Pledge: I pledge my honor that I have abided by the Stevens Honor System

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    return n % 2 == 1

    '''
    101010
    
    If your given number is odd, the rightmost bit would be 1. If your
    given number is even, the rightmost bit would be 2.
    
    Since we read binary from right to left, the value of of the binary
    number would change. When we get eliminate the rightmost number the
    value undergoes integer division. Value // 2.

    If N is odd, then it is easy to find the base case of N since all we
    would need to do is integer divide by 2 and add '1' to the final string.
    Similarly, if N is even, you would add '0' to the final string. 
    '''
    


def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative
    integer n. If n is 0, the empty string is returned.'''

    if n == 0:
        return ''
    elif isOdd(n):
        return numToBinary(n//2) + '1'
    else:
        return numToBinary(n//2) + '0'



def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    elif s[-1] == '1':
        return 1 + binaryToNum(s[:-1]) * 2
    else:
        return binaryToNum(s[:-1]) * 2
                
def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    if s == '11111111':
        return '00000000'
    else:
        x = binaryToNum(s)
        x += 1
        y = 8 - len(numToBinary(x))
        return "0" * y + numToBinary(x)

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    if n == 0:
        print("0" * (8 - len(s)) + s)
    else:
        inc = increment(s)
        print("0" * (8 - len(s)) + s)
        count(inc, n-1)
    

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative
    integer n. If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    elif n % 3 == 2:
        return numToTernary(n//3) + '2'
    elif n % 3 == 1:
        return numToTernary(n//3) + '1'
    else:
        return numToTernary(n//3) + '0'
    
def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    elif s[-1] == '2':
        return 2 + ternaryToNum(s[:-1]) * 3
    elif s[-1] == '1':
        return 1 + ternaryToNum(s[:-1]) * 3
    else:
        return ternaryToNum(s[:-1]) * 3
