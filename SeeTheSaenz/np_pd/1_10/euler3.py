#https://projecteuler.net/problem=3
import pandas as pd
import numpy as np

def find_largest_prime_factor():
    num = 600851475143
    df = pd.DataFrame(sieve_of_erat(), columns=['primes'])
    df['nummodprime'] = num / df['primes']
    df['factors'] = df['nummodprime'] % 1
    df = df[df['factors'] == 0]
    return(df['primes'].max()) 


def sieve_of_erat():
    lst = [i for i in range(2, 10000)]
    for i in lst:
        for val in lst:
            if i == val:
                continue
            elif val % i == 0:
                lst.remove(val)
    return lst
print(find_largest_prime_factor())