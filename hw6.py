'''
Created on 11/6/2023
@author: Lucas Vanzelli and Sargun Cheema
Pledge: I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.



def numToBinary(n, binary = ''):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        final = binary[::-1]
        return (final)
    if n%2 == 0:
        binary += '0'
        return numToBinary(n//2, binary)
    else:
        binary += '1'
        return numToBinary(n//2, binary)

def binaryToNum(s, num = 0):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.'''
    if s == '':
        return num
    elif s[0] == '1':
        binNum = (2**(len(s)-1))
        num += binNum
        return binaryToNum(s[1:], num)
    else:
        return binaryToNum(s[1:], num)

def pad(string):
    '''
    This function adds the necessary amount of zeros to a binary string, string, making
    it a 5 bit binary number.
    '''
    return '0' * (COMPRESSED_BLOCK_SIZE - len(string)) + string

def consec(S, b):
    '''
    This function takes in a binary string, S, and a string, b, which represents either
    a '0', or a '1', and based off of this, counts the number of consecutive times that appears in S.
    '''
    if S == '':
        return 0
    elif S[0] == b:
        return 1 + consec(S[1:], b)
    else:
        return 0




def compress(S):
    '''
    This function takes a string S, which represents a 64 bit and and compresses it
    using run-length encoding.

    The largest number of bits that the compress function could poosibly use to
    encode a 64-bit string/image is 325.
    '''
    if S == '':
        return ''
    else:
        zeros = consec(S[:MAX_RUN_LENGTH], '0')
        if S[zeros:] == '':
            numBinZero = numToBinary(zeros)
            return pad(numBinZero)
   
        ones = consec(S[zeros: zeros + MAX_RUN_LENGTH], '1')
        numBinOne = numToBinary(ones)
        numBinZero = numToBinary(zeros)
    return pad(numBinZero) + pad(numBinOne) + compress(S[zeros + ones:])
       


def uncompress(C):
    '''
    This function takes a run-length encoded compressed bit and outputs the bit
    uncompressed.
    '''
    if C == '':
        return ''
    else:
        zeros = binaryToNum(C[:5])* '0'
        ones = binaryToNum(C[5:10]) * '1'
        return zeros + ones + uncompress(C[10:])


def compression(S):
    '''
    This function takes a bit S and returns the ratio of the compressed size to the
    original size for image S
    '''
    return len(compress(S))/len(S)

'''
We conducted several tests of compress by inputting a series
of random 0s and 1s and then checking the outputs with math to
make sure the function was working properly. We noticed that the
output of the compress function was always larger than the input.

Professor Lai is Lai-ing because you cannot guarentee a shorter bit length for every
possible bit combination. If you do not want to lose some of the information in the
longer bit there must be cases in which a compress file is longer than the original.
For example, the compressed version of the bit '11111100000111' is '001100010100011'.
The original is 14 bits and the compressed version is 15. Unless you cut down the
number of bits in the compressed file, the compressed version of '11111100000111' will
always be greater than the original.
'''
