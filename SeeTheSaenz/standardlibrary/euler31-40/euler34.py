def digitfactorial(limit):
    sum1 = 0
    factorial = 1
    sum2 = 0
    for i in range(3, limit):
        list1 = [int(num) for num in str(i)]
        for n in list1:
            for k in range(1, n + 1):
                factorial = factorial * k
            sum1 = factorial + sum1
            factorial = 1
        if sum1 == i:
            sum2 += i
        sum1 = 0
    return sum2
print(digitfactorial(1000000))
