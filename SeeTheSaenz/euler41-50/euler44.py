def pentagon_number(limit):
    pentagon = {i * (3 * i - 1) // 2 for i in range(1, limit)}
    solution = 0
    for a in pentagon:
        for b in pentagon:
            if a == b:
                break
            if (a + b) in pentagon and (a - b) in pentagon:
                solution = abs(b-a)
    return solution
print(pentagon_number(10000))