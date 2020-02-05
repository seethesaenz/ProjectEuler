from math import factorial

def lattice(x):
    #combination w repitions honerable mention pascals triangle 
    return factorial(x*2) // (factorial(x) * factorial(x))
print(lattice(20))
