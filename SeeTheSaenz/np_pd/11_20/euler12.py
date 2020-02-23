# https://projecteuler.net/problem=12
import pandas as pd
import numpy as np
def euler12(limit):
    trianglelist = [1]
    for i in range(2, limit):
        trianglelist.append(trianglelist[-1] + i)
    df = pd.DataFrame(trianglelist, columns=['triangle'], dtype=np.int64)
    factorlist = [factor(i) for i in trianglelist]
    df['factors'] = factor(df['triangle'])

def factor(num):
    factorlist = [i for i in range(1, num+1) if num % i == 0]
    return len(factorlist)

print(euler12(100000))