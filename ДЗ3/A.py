n = list(map(int, input().split()))

nums = []

for i in range(n[0]):
    nums.append(list(map(int, input().split())))

l = n[1] - 1
r = n[2] - 1

if l == r:
    visited = [True] * n[0]
else:
    visited = [False] * n[0]
    dist = [100000] * n[0]
    dist[l] = 0

i = l

while len(visited) != len(list(filter(lambda x: x is True, visited))):

    for j in range(n[0]):
        if nums[i][j] != -1 and nums[i][j] + dist[i] <= dist[j]:
            dist[j] = nums[i][j] + dist[i]

    visited[i] = True

    target = 100000

    for k in range(len(dist)):
        if dist[k] < target and visited[k] is False:
            i = k
            target = dist[k]

    if target == 100000:
        break

if l == r:
    print("0")
elif dist[r] == 100000:
    print("-1")
else:
    print(dist[r])