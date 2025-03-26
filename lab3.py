"""
Name: Lucas Vanzelli
CS 115 Lab 3
I pledge my honor that I have abided the Stevens Honor System.
"""

def change(amount, coins):
    """
    This function takes two inputs amount and coins where amount
    indicates the amount of money to be made and coins is a list of
    coin values with 1 always being in list when the function is
    first called. It returns a non-negative integer indicating the
    minimum number of coins required to make up the given amount.
    """

    if amount == 0:
        return 0
    if coins == []:
        return float("inf")
    if coins[0] > amount:
        return change(amount, coins[1:])
    else:
        use_it = 1 + change(amount - coins[0], coins)
        lose_it = change(amount, coins[1:])
        return min(use_it, lose_it)
