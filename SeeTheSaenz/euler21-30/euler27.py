import math
def sieve(limit):
    list1 = {}
    for i in range(2, limit + 1):
        list1[i] = True
    for i in list1:
    	if list1[i]:
            if i <= math.sqrt(limit):
                for k in range(i * 2, limit + 1, i):
                    if list1[k]:
                        list1[k] = False
    list2 = [i for i in list1 if list1[i]]
    return list2

def quadraticprime():
    n = 0
    longest = 0
    longesta = 0
    longestb = 0
    for j in range(-1000, 1001):
        for k in sieve(1000):
            test = n ** 2 + j * n + k 
            while checkprime(test) == True:
                n += 1
                test = n ** 2 + j * n + k 
            if n > longest:
                longest = n
                longesta = j
                longestb = k
            n = 0
            test = n ** 2 + j * n + k 
            while checkprime(test) == True:
                n -= 1
                test = n ** 2 + j * n + k 
            if n > longest:
                longest = n
                longesta = j
                longestb = k
            n = 0
            print(longest, longesta, longestb)
    return longesta * longestb

def checkprime(numba):
    if numba % 2 ==0:
        return False
    for i in range(3, numba, 2):
        if numba % i == 0:
            return False
    return True
print(quadraticprime())


