# There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.
import math
import random


def findtriplet():
    # while a+b+c does not equal 1000, this line is where the magic happens really
    while a + b + c != 1000:
        # set a to random int between 1-200 """had to play with the limits using the rule of pythagorean that a<b<c"""
        a = random.randint(1, 200)
        # set b to random int between 200-400
        b = random.randint(200, 400)
        # calculated c squared from a squared + b squared
        cc = math.pow(a, 2) + math.pow(b, 2)
        # square rooted c squared and set to C
        c = math.sqrt(cc)
    # prints the product of abc
    print(int(a * b * c))


findtriplet()
