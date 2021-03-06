import math
def summationOfPrimes(limit):
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
    return sum(list2)

summationOfPrimes(200000)