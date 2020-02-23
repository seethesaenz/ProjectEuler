import numpy as np
import pandas as pd
def euler9():
    arr = np.array(np.arange(1, 501), dtype=np.int64)
    for a in arr[0:250]:
        for b in arr[200:500]:
            if a > b:
                continue
            cc = pow(a, 2) + pow(b, 2)
            c = cc ** 0.5
            if c + b + a == 1000 and c > b and c % 1 == 0:
                return int(a * b * c), a, b, int(c) 
print(euler9())
