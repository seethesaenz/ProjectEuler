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

def pandigitalprime():
    check = []
    test = []
    largest = 0
    primelist = sieve(10000000)
    for prime in primelist:
        for i in range(1, len(str(prime))+1):
            check.append(i)
        for char in str(prime):
            test.append(int(char))
        test.sort()
        print(test, check)
        if test == check and largest < prime:
            largest = prime
        test.clear()
        check.clear()
    return largest
print(pandigitalprime())

            

