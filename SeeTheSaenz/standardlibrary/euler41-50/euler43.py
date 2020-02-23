from itertools import permutations
def substring_divisibility():
    pandig = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    test = [3, 5, 7, 11, 13, 17]
    perms = permutations(pandig)
    digits = []
    answer = []


    for perm in perms:
        if int(perm[3]) % 2 == 0:
            digits.append(perm)
    for perm in digits:
        for i, el in enumerate(test):
            tmp = int(''.join(perm[2+i:5+i]))
            if tmp % el == 0:
                continue
            else:
                break
        else:
            numba = ''
            for char in perm:
                numba = numba + char
            answer.append(int(numba))
    return answer, sum(answer)
print(substring_divisibility())
