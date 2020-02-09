def factorialdigitsum(num):
    factorial = 1
    sum = 0
    for i in range(1, num+1):
        factorial = factorial * i
    for i in str(factorial):
        sum = int(i) + sum
    return sum
print(factorialdigitsum(100))