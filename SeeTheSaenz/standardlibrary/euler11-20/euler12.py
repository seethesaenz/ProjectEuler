# https://projecteuler.net/problem=12
import math


def factorTriangles():
    list1 = [1]
    factorlist = []
    count = 2
    # while the length of factor list is less than 500
    while len(factorlist) < 500:
        # check the problem to see the sequence that im creating
        list1.append(list1[-1] + count)
        count += 1
        countDiv = 1
        # this is doing all the factoring i originally had something much less efficient and sucked
        while countDiv <= math.sqrt(list1[-1]):
            # checking to see if the count is a factor
            if list1[-1] % countDiv == 0:
                # if its a factor and a square just append once
                if list1[-1] // countDiv == countDiv:
                    factorlist.append(countDiv)
                # if its not square it appends both the divisor and the quotient saving lots of loops if i just 
                # itered through the whole num 
                else:
                    factorlist.append(countDiv)
                    factorlist.append(list1[-1] // countDiv)
            countDiv += 1
        # if factor list is not long enough the reset factor list
        if len(factorlist) < 500:
            factorlist = []
    print(list1[-1], len(factorlist))


factorTriangles()
