def collatz():
    chain = []
    longest = 0
    longestnumber = 0
    for i in range(2, 1000001):
        while i > 1:
            chain.append(i)
            if i % 2 == 0:
                i //= 2
            elif i % 2 == 1:
                i = 3*i + 1
        if longest < len(chain):
            longest = len(chain)
            longestnumber = chain[0]
        chain.clear()
        print(longest, longestnumber)
    return longest, longestnumber
print(collatz())