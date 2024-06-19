#!/usr/bin/python3
"""Module of  making change"""


def makeChange(coins, total):
    """Determines the fewest number of
    coins needed to meet a given
    amount total"""
    if total <= 0:
        return 0

    total_now = 0
    used_coins = 0
    coins = sorted(coins, reverse=True)
    for c in coins:
        r = (total - total_now) // c
        total_now += r * c
        used_coins += r
        if total_now == total:
            return used_coins
    return -1
