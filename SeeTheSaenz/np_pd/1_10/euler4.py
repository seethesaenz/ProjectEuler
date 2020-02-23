import pandas as pd
import numpy as np

def find_largest_palindrome(lowerlimit, upperlimit):
    ls = [i for i in range(lowerlimit, upperlimit, 1)]
    products = [x*y for x in ls for y in ls]
    df = pd.DataFrame(products, columns=['col1'])
    reverse = [int(str(i)[::-1]) for i in products]
    df['reversed'] = reverse
    # df1['pricesMatch?'] = np.where(df1['Price1'] == df2['Price2'], 'True', 'False')
    df['prod'] = np.where(df['col1'] == df['reversed'], 'True', 'False')
    palindromes = [df['col1'].iloc[i] for i, el in enumerate(df['prod']) if el == 'True']

    return(max(palindromes))


print(find_largest_palindrome(100, 1000))