# Problem:
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# Solution Efficiency:
# O(n^2), would be more efficient to generate primes, rather than count up to n; but this would still be O(n^2)

from collections import deque
import time

def algo(n):
    i = 2
    lastPrime = 0
    while n > 1:
        #print(f"i: {i}, n: {n}")
        if n % i == 0:
            lastPrime = i
            n = n // i
            i = 2
        i += 1
    return lastPrime

if __name__ == "__main__":
    n = 600851475143
    start_time = time.time()
    output = algo(n)
    timeDiff = time.time() - start_time
    print(f"biggest factor of {n}: {output}")
    print(f"runtime: {timeDiff}")