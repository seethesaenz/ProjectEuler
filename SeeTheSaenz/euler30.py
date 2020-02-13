def digitfifth():
    sum1 = 0
    sumonumbas = 0
    for i in range(2, 1000000):
        for n in str(i):
            sum1 = sum1 + int(n)**5
        if sum1 == i:
            sumonumbas = sumonumbas + i
        sum1 = 0
    return sumonumbas
print(digitfifth())
