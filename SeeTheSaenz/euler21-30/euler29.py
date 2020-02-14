def distictpowers():
    list1 = []
    for a in range(2, 101):
        for b in range(2, 101):
            list1.append(a ** b)
    list1 = set(list1)
    return len(list1)
print(distictpowers())