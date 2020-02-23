#https://projecteuler.net/problem=6
import pandas as pd
import numpy as np
def euler6():
    df = pd.DataFrame(np.arange(1, 101), columns=['nums'])
    df['squared'] = df['nums'] ** 2
    return (df['squared'].sum() - ((df['nums'].sum()) ** 2))
print(euler6())