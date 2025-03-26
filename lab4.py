'''
Created on 10/5/2023
@author: Lucas Vanzelli
Pledge: I pledge my honor that I have abided by the Steven Honor System.
CS115 - Lab 4
'''

def knapsack(capacity, itemList):
    '''
    This function takes the parameters capacity and itemList. It returns
    both the maximum value and the list of items that make this value,
    without exceeding the capacity of the knapsack.
    '''
    if capacity <= 0 or itemList == []:
        return [0, []]
    elif itemList[0][0] > capacity:
        return knapsack(capacity, itemList[1:])
    else:
        slay = knapsack(capacity - itemList[0][0], itemList[1:])
        use_it = [slay[0] + itemList[0][1], [itemList[0]] + slay[1]] 
        lose_it = knapsack(capacity, itemList[1:])
        if use_it[0] > lose_it[0]:
            return use_it
        else:
            return lose_it
        
