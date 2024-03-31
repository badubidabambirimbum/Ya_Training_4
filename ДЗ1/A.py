n = int(input())
nums = list(map(int, input().split()))
x = int(input())

def partition(nums, x):

    E = []
    G = []
    N = []

    for i in range(n):
        if nums[i] < x:
            E.append(nums[i])
        elif nums[i] > x:
            N.append(nums[i])
        else:
            G.append(nums[i])

    return len(E + G + N) - len(N+G)

target = partition(nums,x)

print(target)
print(n-target)