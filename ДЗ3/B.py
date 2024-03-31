n = list(map(int, input().split()))

nums = []

for i in range(n[0]):
    nums.append(list(map(int, input().split())))

l = n[1] - 1
r = n[2] - 1

visited = [False] * n[0]
dist = [100000] * n[0]
dist[l] = 0
path = [-1] * n[0]

i = l

while len(visited) != len(list(filter(lambda x: x is True, visited))):

    for j in range(n[0]):
        if nums[i][j] != -1 and nums[i][j] + dist[i] < dist[j]:
            dist[j] = nums[i][j] + dist[i]
            path[j] = i

    visited[i] = True

    target = 100000

    for k in range(len(dist)):
        if dist[k] < target and visited[k] is False:
            i = k
            target = dist[k]

    if target == 100000:
        break

result = []
i = r

while path[i] != -1:
    result.append(i+1)
    i = path[i]

if path[r] != -1 or l == r:
    result.append(l+1)
else:
    result.append(-1)

print(*list(reversed(result)))