from time import time
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

def circularprimes(limit):
    primes = prime_list(limit)
    count = 0
    for prime in primes:
        k = str(prime)
        for rotates in range(len(str(prime))):
            if int(k) in primes:
                print(k, count)
                last = k[len(k)-1:len(k)]
                first = k[0:len(k)-1]
                k = last+first
            else:
                break
        else:
            count += 1
    return count
start_time = time()
print(circularprimes(1000000))
passed_time = time()-start_time
print(passed_time)