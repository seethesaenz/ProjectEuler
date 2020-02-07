import math
num = 600851475143
numtest = 21002
num1 = 12

def primefactor(number):
    factors=[]
    while(number>1):
        factor = getFactors(number)
        factors.append(factor)
        number //= factor
    return factors


def getFactors(number):
    if number % 2 ==0:
        return 2
    for x in range(3, int(math.sqrt(number))+1, 2):
        if number % x == 0:
            return x
    return number
print(primefactor(num))
