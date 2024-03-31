import heapq

n = int(input())

start_end = list(map(int, input().split()))

m = int(input())

nums = {i: [] for i in range(n)}

for i in range(m):
    lst = list(map(int, input().split()))
    nums[lst[0]-1].append([lst[1],lst[2]-1,lst[3]])

l = start_end[0] - 1
r = start_end[1] - 1

visited = [False] * n
dist = [10 ** 15] * n
dist[l] = 0

i = l

h = list()
h.append([0, l])

heapq.heapify(h)
heapq.heappop(h)
heapq.heappush(h, [10**15, 0])

while len(h) != 0:

    for j in range(len(nums[i])):
        if nums[i][j][0] >= dist[i] and nums[i][j][2] < dist[nums[i][j][1]] and i != nums[i][j][1]:
            dist[nums[i][j][1]] = nums[i][j][2]

            if visited[i] is False:
                heapq.heappush(h, [dist[nums[i][j][1]], nums[i][j][1]])

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