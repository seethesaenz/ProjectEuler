#https://projecteuler.net/problem=7
def euler7(limit):
    hashtbl = [1] * limit
    for el, val in enumerate(hashtbl):
        if el == 0 or el == 1:
            hashtbl[el] = 0
            continue
        if val:
            for i in range(el*2, limit, el):
                hashtbl[i] = 0
    primes = [i for i, el in enumerate(hashtbl) if el]
    return sum(primes)
print(euler7(2000000))
