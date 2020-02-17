tree_list = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20,  4, 82, 47, 65],
    [19,  1, 23, 75,  3, 34],
    [88,  2, 77, 73,  7, 63, 67],
    [99, 65,  4, 28,  6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]
]

tmp_list = [
    [3],
    [7, 4],
    [2, 4, 6],
    [8, 5, 9, 3],
]


def maxpathsum(tree):
    for row in tree:
        if len(row) == 1:
            continue
        elif len(row) == 2:
            for i in range(len(row)): 
                tree[(len(row)-1)][i] = tree[(len(row)-1)][i] + tree[0][0]
        elif len(row) > 2:
            previousrow = tree[len(row)-2]
            for i in range(len(row)):
                if i == 0:
                    tree[len(row)-1][i] = tree[len(row)-1][i] + previousrow[0]
                elif 0 < i < len(row)-1:
                    if previousrow[i-1] > previousrow[i]:
                        tree[len(row)-1][i] = tree[len(row)-1][i] + previousrow[i-1]
                    else:
                        tree[len(row)-1][i] = tree[len(row)-1][i] + previousrow[i]
                else:
                    tree[(len(row)-1)][i] = tree[(len(row)-1)][i] + previousrow[-1]
    

    return max(tree[-1])
print(maxpathsum(tree_list))