def pandigitalproducts():
    answer = set()
    for a in range(1, 2000):
        a_str = str(a)
        if len(a_str) != len(set(a_str)) or '0' in a_str:
            continue
        for b in range(1, 2000):
            b_str = str(b)
            ab_str = str(a*b)
            if len(b_str) != len(set(b_str)) or '0' in b_str or '0' in ab_str:
                continue
            var = a_str + b_str + str(a * b)
            if len(set(var)) == len(var) == 9:
                answer.add(a*b)
    return sum(answer)
print(pandigitalproducts())