#https://projecteuler.net/problem=2
import pandas as pd
import numpy as np

def euler2():
    fibonacci = [0, 1]
    while fibonacci[-1] < 4000000:
        fibonacci.append(fibonacci[-2] + fibonacci[-1])
    if fibonacci[-1] > 4000000:
        fibonacci.pop()
    df = pd.DataFrame(fibonacci, columns=['num'])
    df['even'] = df['num'] % 2
    df['num'] = df[df['even'] == 0]
    print(df['num'].sum())
euler2()