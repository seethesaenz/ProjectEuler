import pathlib
triangle = pathlib.Path('C:/Users/jack/Documents/Euler/SeeTheSaenz/p067_triangle.txt').expanduser().resolve()
with triangle.open('r') as t_fd:
    triangle_list = [[int(c) for c in line.strip().split(' ')] for line in t_fd.readlines()]

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
print(maxpathsum(triangle_list))