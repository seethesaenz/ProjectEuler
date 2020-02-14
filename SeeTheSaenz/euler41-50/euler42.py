import pathlib

def trianglewords():
    fileword = pathlib.Path('C:\Users\jack\Documents\Euler\SeeTheSaenz\euler41-50\p042_words.txt').expanduser().resolve()
    with fileword.open('r') as t_fd:
        words = [[c for c in line.strip().split(',')] for line in t_fd.readlines()]

print(trianglewords())