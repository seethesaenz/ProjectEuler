import pathlib
import string

def trianglewords():
    fileword = pathlib.Path('euler41-50/p042_words.txt').expanduser().resolve()
    with fileword.open('r') as t_fd:
        words = [s.strip('"') for line in t_fd.readlines() for s in line.strip().split(',')]

    triangle_numbers = [int(0.5 * i * (i + 1)) for i in range(1, 10000)]
    alpha_dict = {c: i + 1 for i, c in enumerate(string.ascii_uppercase)}
    counter = 0
    for word in words:
        val = 0
        for char in word:
            val += alpha_dict[char]
        if val in triangle_numbers:
            counter += 1
    print(counter)

print(trianglewords())