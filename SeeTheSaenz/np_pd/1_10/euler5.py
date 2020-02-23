#https://projecteuler.net/problem=5
def euler5():
    count = 0
    value = 2520
    tmp = 0
    boolin = True
    ls = [i for i in range(20, 0, -1)]
    while boolin:
        count = 0
        for i in ls:
            tmp = value
            value += value % i
            if tmp == value:
                count += 1 
        if count == 20:
            boolin = False
    return value
print(euler5())