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

def upper_bound(coins):
    """Determines the maximum value that needs to be checked to
    prove coins canonical."""
    raise NotImplementedError("TODO")

def greedy(coins, value):
    """Determines the number of coins the greedy algorithm uses
    to make change for value."""
    raise NotImplementedError("TODO")

def dynamic(coins, value):
    """Determines the optimal number of coins to make change for value."""
    raise NotImplementedError("TODO")

def main():
    coins = read_input()
    #TODO: call your greedy and dynamic functions on 1...upper_bound

if __name__ == "__main__":
    main()
