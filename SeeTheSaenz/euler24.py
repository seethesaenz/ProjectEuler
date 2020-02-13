from itertools import permutations
def lexicoperms():

    l = list(permutations(range(0, 4)))
    l = str(l).replace('(', '[').replace(')',']')
    l[0] = ' '
    l[-1] = ' '
    print(l)
print(lexicoperms())
    