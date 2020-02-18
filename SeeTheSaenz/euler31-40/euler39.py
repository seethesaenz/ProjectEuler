import math
def right_triangle(limit):
    solutions = set()
    for b in range(1, limit):
        for a in range(1, limit):
            if a > b:
                break
            aa = a * a
            bb = b * b
            cc = aa + bb
            c = math.sqrt(cc)
            if b > c:
                break
            perim = int(c) + a + b
            if perim <= limit and c % 1 == 0:
                tup = a, b, int(c), perim
                solutions.add(tup)
    my_dict = {}
    for solution in solutions:
        if solution[3] not in my_dict:
            my_dict[solution[3]] = 1
        else:
            my_dict[solution[3]] = my_dict[solution[3]] + 1
    return max(my_dict, key=lambda k: my_dict[k])
print(right_triangle(1000000))