def tri_pent_hex(limit):
    triangle = [i * (i + 1) // 2 for i in range(1, limit)]
    pentagonal = [i * (3 * i - 1) // 2 for i in range(1, limit)]
    hexagonal = [i * (2 * i - 1) for i in range(1, limit)]
    biglist = triangle + pentagonal + hexagonal
    triangle.clear()
    pentagonal.clear()
    hexagonal.clear()
    hashtbl = [0] * (max(biglist)+1)
    for i in range(0, len(biglist)):
        hashtbl[biglist[i]] += 1
    solutions = set()
    for i in range(0, len(biglist)):
        if (hashtbl[biglist[i]] > 2):
            solutions.add(biglist[i])
    return solutions
print(tri_pent_hex(60000))