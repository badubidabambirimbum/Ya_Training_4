import random

n = int(input())

if n == 0:
    print()
else:
    nums = list(map(int, input().split()))

    def partition(nums, x, l, r):

        E = []
        G = []
        N = []

        for i in range(l, r + 1):
            if nums[i] < x:
                E.append(nums[i])
            elif nums[i] > x:
                N.append(nums[i])
            else:
                G.append(nums[i])

        nums[l:r + 1] = E + G + N

        return len(E + G + N) - len(N + G) + l

    def quicsort(nums, l, r):
        if l >= r:
            return 0
        x = nums[random.randint(l, r - 1)]
        p = partition(nums, x, l, r)
        quicsort(nums, l, p)
        quicsort(nums, p + 1, r)

    l = 1
    while l < n and nums[l - 1] <= nums[l]: l += 1
    if l != n:
        quicsort(nums,0,n-1)

    print(*nums)