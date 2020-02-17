from fractions import Fraction
def digit_cancelling_fractions():
    possible = []
    for num in range(10, 100):
        n_str = str(num)
        if len(set(n_str)) != len(n_str):
            continue
        for den in range(10, 100):
            d_str = str(den)
            if num == den or len(set(d_str)) != len(d_str) or den % 10 == 0:
                continue
            if (n_str[0] in d_str):
                d_str = d_str.replace(n_str[0], '')
                n_str1 = n_str.replace(n_str[0], '')
            elif(n_str[1] in d_str):
                d_str = d_str.replace(n_str[1], '')
                n_str1 = n_str.replace(n_str[1], '')
            if Fraction(num, den) == Fraction(int(n_str1), int(d_str)):
                possible.append(Fraction(num, den))
    total = Fraction(1, 1)
    for frac in possible:
        if frac < 1:
            total *= frac
    return total.denominator
print(digit_cancelling_fractions())