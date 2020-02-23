def prime_list(n):
    marked = [0] * n
    value = 3
    my_list = [2]
    while value < n:
        if marked[value] == 0:
            my_list.append(value)
            i = value
            while i < n:
                marked[i] = 1
                i += value
        value += 2
    return my_list

def goldbach_other_conj(limit):
    primes = prime_list(limit)
    odd_composites = {i for i in range(2, limit) if i % 2 != 0}
    for prime in primes:
        if prime in odd_composites:
            odd_composites.remove(prime)
    for el in odd_composites:
        othercheck = False
        count = 0
        while othercheck == False:
            for prime in primes:
                for i in range(1, 100):
                    if (prime + (2 * i ** 2)) == el:
                        othercheck = True
            print(el)
            count +=1
            if count > 5:
                return el

goldbach_other_conj(10000)
