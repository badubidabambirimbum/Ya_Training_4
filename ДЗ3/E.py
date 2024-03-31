from collections import deque

n = int(input())

drivers = []

for i in range(n):
    drivers.append(list(map(int, input().split())))

nums = {i: [] for i in range(n)}

for i in range(n-1):
    lst = list(map(int, input().split()))
    nums[lst[0] - 1].append([lst[1]-1,lst[2]])
    nums[lst[1] - 1].append([lst[0]-1, lst[2]])

ns = []

start = 0
end = 0

def bfs(graph, vertex,m):
    queue = deque([vertex])
    visited = {vertex: True}
    dist = [0] * m
    while queue:
        v = queue.popleft()
        for n in range(len(graph[v])):
            if graph[v][n][0] not in visited:
                dist[graph[v][n][0]] = dist[v] + graph[v][n][1]
                queue.append(graph[v][n][0])
                visited[graph[v][n][0]] = True
    return dist

for i in range(n):
    l = bfs(nums, i, n)
    ns.append(l)

res = {}
tg = 0


i = start

visited = [False] * n
dist = [10 ** 15] * n
dist[i] = 0
path = [-1] * n

while visited[i] != True:

    for j in range(n):

        if ns[i][j] != -1 and dist[i] + (ns[i][j] / drivers[j][1]) + drivers[j][0] < dist[j]:
            dist[j] = dist[i] + (ns[i][j] / drivers[j][1]) + drivers[j][0]
            path[j] = i

    visited[i] = True

    target = 10**15

    for k in range(len(dist)):
        if dist[k] < target and visited[k] is False:
            i = k
            target = dist[k]

    if target == 10**15:
        break

tg = 0

for k in range(len(dist)):
    if dist[k] > tg:
        i = k
        tg = dist[k]

result = []

while path[i] != -1:
    result.append(i+1)
    i = path[i]

if path[end] != -1 or start == end:
    result.append(start+1)
else:
    result.append(-1)

print(tg)
print(*result)