def spiraldiag(length):
    if length % 2 == 0:
        return 'length must be odd!'
    diag = [1]
    count = 2
    num = ((length-1) * 2) + 1
    while len(diag) < num:
        for i in range(4):
            diag.append(diag[-1] + count)
        count += 2
    summation = sum(diag)
    return summation
print(spiraldiag(1001))