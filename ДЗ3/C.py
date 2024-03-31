import heapq

n = list(map(int, input().split()))

nums = {i: [] for i in range(n[0])}

for i in range(n[1]):
    lst = list(map(int, input().split()))
    nums[lst[0]-1].append([lst[1]-1,lst[2]])
    nums[lst[1]-1].append([lst[0]-1,lst[2]])


m = list(map(int, input().split()))

l = m[0] - 1
r = m[1] - 1

visited = [False] * n[0]
dist = [10 ** 15] * n[0]
dist[l] = 0

i = l

h = list()
h.append([0, l])

heapq.heapify(h)
heapq.heappop(h)
heapq.heappush(h, [10**15, 5])

while len(h) != 0:

    for j in range(len(nums[i])):
        if nums[i][j][1] + dist[i] < dist[nums[i][j][0]]:
            dist[nums[i][j][0]] = nums[i][j][1] + dist[i]
            if visited[nums[i][j][0]] is False:
                heapq.heappush(h, [dist[nums[i][j][0]], nums[i][j][0]])

    visited[i] = True

    while visited[i] == True:

        if len(h) == 0:
            break

        i = h[0][1]
        target = h[0][0]
        heapq.heappop(h)

    if target == 10 ** 15:
        break

if l == r:
    print("0")
elif dist[r] == 10 ** 15:
    print("-1")
else:
    print(dist[r])