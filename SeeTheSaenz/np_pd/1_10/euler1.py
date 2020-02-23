# https://projecteuler.net/problem=1
import numpy
import pandas as pd
def euler1():
    lst = numpy.arange(1000)
    df = pd.DataFrame(lst, columns=['num'])
    df['mod3'] = df['num'] % 3
    df['mod5'] = df['num'] % 5
    df['num'] = df[(df['mod3'] == 0) | (df['mod5'] == 0)]
    print(df['num'].sum())
    
euler1()

