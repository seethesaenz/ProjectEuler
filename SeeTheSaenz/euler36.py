def doublebasepalindrome(limit):
    sum1 = 0
    for num in range(1, limit + 1):
        base10 = [int(i) for i in str(num)]
        base10R = base10[::-1]
        if base10R == base10:
            bin1 = bin(num)[2:]
            base2 = [int(i) for i in str(bin1)]
            base2R = base2[::-1]
            if base2 == base2R:
                sum1 = sum1 + num
    return sum1
print(doublebasepalindrome(1000000))