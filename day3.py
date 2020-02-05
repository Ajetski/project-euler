# Problem:
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# Solution Efficiency:
# O(n^2), would be more efficient to generate primes, rather than count up to n; but this would still be O(n^2)

from collections import deque

def algo(n, primes):
    i = 2
    while n > 1:
        print(f"i: {i}, n: {n}")
        if n % i == 0:
            primes.append(i)
            n = n // i
            i = 2
        i += 1
    return primes

if __name__ == "__main__":
    value = algo((600851475143), deque())
    print(value)
    product = 1
    for e in value:
        product *= e
    print(f"product of deque: {product}")