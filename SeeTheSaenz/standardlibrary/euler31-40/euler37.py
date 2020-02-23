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

def truncatable_primes(n):
    primes = prime_list(n)
    pre_suf = ['2', '3', '5', '7']
    possible_primes = [i for i in primes if str(i)[0] in pre_suf and str(i)[-1] in pre_suf]
    for i in [2, 3, 5, 7]:
        possible_primes.remove(i)
    possible_primes1 = []
    for prime in possible_primes:
        tmp = str(prime)
        for _ in range(len(str(prime))-1):
            tmp = tmp[1:]
            if int(tmp) in primes:
                continue
            break
        else:
            tmp = str(prime)  
            for __ in range(len(str(prime))-1):
                tmp = tmp[:-1]
                if int(tmp) in primes:
                    continue
                break
            else:
                possible_primes1.append(prime)

    return sum(possible_primes1)

print(truncatable_primes(1000000))
    