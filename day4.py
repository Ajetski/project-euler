# Problem:
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

import time

# this is not a good general solution, but works well for this specific problem.
# the odds that the palindrome will exist as a * b for some integers a and b > 900 is likely

def isPalindrome(n):
    string = str(n)
    startIdx = 0
    endIdx = len(string) - 1
    while startIdx < endIdx:
        if string[startIdx] != string[endIdx]:
            return False
        startIdx += 1
        endIdx -= 1
    return True

def algo():
    first = 999
    second = 999
    n = 100
    while first > 900:
        while second > 900:
            if isPalindrome(first * second):
                return first * second
            second -= 1
        second = 999
        first -= 1

if __name__ == "__main__":
    start = time.time()
    value = algo()
    timeDiff = start - time.time()
    print(f"result: {value}")
    print(f"runtime: {timeDiff}")