#! /usr/bin/env python3
"""
coins.py --- starter file for the canonical coins problem

This program reads a set of coins from standard input.
You need to modify this program to determine whether the
set of coins is canonical. Then it should print one of:
-- CANONICAL (and the numbers checked to prove it)
-- NON-CANONICAL (and the smallest number where greedy fails)

Example Usage: ./coins.py < coins1.txt
"""

import sys

def read_input():
    data = sys.stdin.read().strip()
    coins = [int(c) for c in data.split()]
    return coins

def upper_bound(coins):
    """Determines the maximum value that needs to be checked to
    prove coins canonical."""
    return sum(coins[i] * (coins[i +1] - 1) for i in range(len(coins) - 1))

def greedy(coins, value):
    """Determines the number of coins the greedy algorithm uses
    to make change for value.
    
    params:
        coins: list of coin denominations
        value: change to make

    returns:
        int: number of coins

        Can we assume that we are also able to make correct change?
    """
    change = value

    num_coins = 0
    for coin in coins[::-1]:
        if change <= 0:
            break
        if change >= coin:
            num_coins += change//coin
            change = change % coin
    
    return num_coins

def get_min(coins, change_list, current_change):
    min_value = float('inf')

    for coin in coins:
        if current_change - coin >= 0:
            if change_list[current_change - coin] < min_value:
                min_value = change_list[current_change - coin]

    return min_value

def dynamic(coins, value):
    """Determines the optimal number of coins to make change for value.
    
     
    params:
        coins: list of coin denominations
        value: change to make

    returns:
        int: number of coins
    """
    change = value

    change_list = [0] * (change + 1)

    for i in range(1, change + 1):
        change_list[i] = 1 + get_min(coins, change_list, i)

    return change_list[-1]


def main():
    coins = read_input()
    upper = upper_bound(coins)

    for i in range(1, upper + 1):
        if dynamic(coins, i) != greedy(coins, i):
            print("NON-CANONICAL")
            print('fails on n={}'.format(i))
            return

    print('CANONICAL')

if __name__ == "__main__":
    main()
