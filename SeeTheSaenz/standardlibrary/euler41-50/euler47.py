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
    return primes

def euler47():
    primes = euler7(1000000)
    consecutive = 0
    for i in range(1, 100000):
        if prime_factorization(i, primes)

def prime_factorization(num, primes):
    primefactorlist = []
    i = 2
    while i == 2:
        for prime in primes:
            if num % prime == 0:
                primefactorlist.append(prime):
                num //= prime
            else:
                i = 1
    if num == 1:
        return True
    else:
        return False
