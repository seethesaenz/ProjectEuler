def find_factors(top_num):
    factors = []
    for i in range(1, top_num):
        div, mod = divmod(top_num, i)
        if mod == 0:
            if div not in factors:
                factors.append(div)
            if i not in factors:
                factors.append(i)
    while top_num in factors:
        factors.remove(top_num)
    return factors

def nonabundantsums():
    abundant = []
    for i in range(2, 28124):
        factor = find_factors(i)
        print(i)
        if sum(factor) > i:
            abundant.append(i)
    abundant = set(abundant)
    number = [i for i in range(1, 28124)]
    for i in abundant:
        for k in abundant:
            if i+k in number:
                print(i+k)
                number.remove(i+k)
    return sum(number)
print(nonabundantsums())
          
    