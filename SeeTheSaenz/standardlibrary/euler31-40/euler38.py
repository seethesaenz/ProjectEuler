def pandigitalmultiplees(limit):
    count = 0
    bignum = ''
    biggest = 0
    for i in range(1, limit):
        num = i
        while len(bignum) < 9:
            count += 1
            num = i * count
            bignum = bignum + str(num)
        if len(bignum) > 9:
            num = 0
            count = 0
            bignum = ''
            continue
        num = 0
        if '1' in bignum and '2' in bignum and '3' in bignum and '4' in bignum and '5' in bignum and '6' in bignum and '7' in bignum and '8' in bignum and '9' in bignum:
            x = True
        else:
            x = False
        if x and int(bignum) > biggest:
            biggest = int(bignum)
            number = i
            n = count
            x = False
        bignum = ''
        count = 0
    return biggest, number, n
print(pandigitalmultiplees(1000000))
