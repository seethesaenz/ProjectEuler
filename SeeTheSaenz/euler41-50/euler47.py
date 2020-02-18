def prime_list(n):
    marked = [0] * n
    value = 3
    my_list = [2]
    while value < n:
        if marked[value] == 0:
            my_list.append(value)
            i = value
            while i < n:
                marked[i] = 1
                i += value
        value += 2
    return my_list

