#There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.
import math
import random

def findtriplet():
    a=0
    b=0
    c=0
    while(a + b + c != 1000):
        a = random.randint(1, 200)
        b = random.randint(200, 400)
        cc = math.pow(a, 2) + math.pow(b, 2)
        c = math.sqrt(cc)
    print(int(a*b*c))

findtriplet()


