N = int(input())
matrix = list()
mins = [10**15] * N
for i in range(N):
    matrix.append(list(map(int, input().split())))
    for j in range(len(matrix[0])):
        if matrix[i][j] != 0 and mins[i] > matrix[i][j]:
            mins[i] = matrix[i][j]

min_down = sum(mins)
target = -1
best = 10**15

def rec(a,l,N,count,min,s:set):
    global mins
    global target
    global best

    s.add(a)
    l += 1

    if l == N:
        if count + matrix[0][a] < best and matrix[0][a] > 0:
            target = count + matrix[0][a]
            best = target
        return 0

    for i in range(len(matrix[0])):
        if matrix[a][i] > 0 and len(s & set([i])) == 0:
            l_rec = l
            count_rec = count + matrix[a][i]
            min_rec = min
            s_rec = set(s)
            rec(i,l_rec,N,count_rec,min_rec,s_rec)

rec(0, l=0, N=N, count=0,min=min_down,s = set())

if N == 1:
    print(0)
else:
    print(target)