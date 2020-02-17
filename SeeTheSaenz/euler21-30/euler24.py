from itertools import permutations
def lexicographicperm(n):
    numba = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    perms = permutations(numba)
    nums = []
    for perm in perms:
        num = int(''.join(perm))
        nums.append(num)
    nums = sorted(nums)
    return nums[n-1]
print(lexicographicperm(1000000))