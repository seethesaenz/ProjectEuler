#https://projecteuler.net/problem=50
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

def euler50():
    primes = euler7(1000000)
    value = 0
    primeset = set(primes)
    longestconsecutive = 0
    for i in range(0, len(primes)):
        for x in range(i+1, len(primes)):
            if sum(primes[i:x])> 1000000:
                break
            value = sum(primes[i:x])
            if value in primeset:
                consecutive = x-i
                if longestconsecutive < consecutive:
                    biggestsum = value
                    longestconsecutive = consecutive
                    strip = primes[i:x]
            value = 0
    return biggestsum, longestconsecutive

print(euler50())
