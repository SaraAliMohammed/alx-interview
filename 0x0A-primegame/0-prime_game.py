#!/usr/bin/python3
"""Define isWineer function, a solution to the Prime Game problem"""


def primes_numbers(n):
    """Return list of prime numbers between 1 and n inclusive
       Args:
        n (int): the upper boundary of range. lower boundary is always 1
    """
    primes = []
    sieve = [True] * (n + 1)
    for prime in range(2, n + 1):
        if (sieve[prime]):
            primes.append(prime)
            for index in range(prime, n + 1, prime):
                sieve[index] = False
    return primes


def isWinner(x, nums):
    """
    Determines the winner of the Prime Game
    Args:
        x (int): rounds number.
        nums (int): the upper limit of the range for each round
    Return:
        Name of winner (Maria or Ben) or None if winner cannot be found
    """
    if not x or not nums or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        prime = primes_numbers(nums[i])
        if len(prime) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
