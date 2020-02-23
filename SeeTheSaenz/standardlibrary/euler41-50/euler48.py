# https://projecteuler.net/problem=48
def selfpowers():
    lst = [pow(i, i) for i in range(1, 1001)]
    return (sum(lst) % pow(10, 10))
print(selfpowers())