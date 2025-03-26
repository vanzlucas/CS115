'''
Created on 10/1/2023
@author: Lucas Vanzelli & Janet Koublanou
Pledge: I pledge my honor that I have abided by the Stevens Honor System.
CS115 - Hw 2
'''
import sys
# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# Implement your functions here.

def letterScore(letter, scorelist):
    '''
    This function takes a letter and a list of letters, with their
    corresponding scores, and returns the score of the first parameter.
    '''
    if letter == scorelist[0][0]:
        return scorelist[0][1]
    else:
        return 0 + letterScore(letter, scorelist[1:])

def wordScore(S, scorelist):
    '''
    This function takes a string S and a scorelist, mentioned previously,
    and returns the score value of the string S.
    '''
    if S == "":
        return 0
    else:
        return letterScore(S[0], scorelist) + wordScore(S[1:], scorelist)

def wordInRack(word, Rack):
    '''
    This function takes a hypothetical word called word and a Rack of
    words and returns True or False whether or not that word can be made
    by the given Rack.
    '''
    if word[0] in Rack and len(word) == 1:
        return True    
    elif word[0] in Rack:
        index = Rack.index(word[0])
        return wordInRack(word[1:], Rack[:index] + Rack[index + 1:])
    else:
        return False


def scoreList(Rack):
    '''
    Takes an input Rack and returns a list of all of the words in the global
    Dictionary that can be made from those letters and the score for each one.
    '''
    name = filter(lambda x: wordInRack(x, Rack), Dictionary)
    return list(map(lambda word: [word, wordScore(word,scrabbleScores)], name))

def chooseWord(finalList):
    '''
    This function takes the input finalList and returns a list containing
    the word with the highest scrabble value.
    '''
    if finalList == []:
        return ['', 0]
    else:
        use = finalList[0]
        lose = chooseWord(finalList[1:])
        if max(use[1], lose[1]) == lose[1]:
            return lose
        else:
            return use

def bestWord(Rack):
    '''
    Takes an input Rack and returns a list with two elements: the highest
    possible scoring word from that Rack followed by its score.
    '''
    return chooseWord(scoreList(Rack))


    
