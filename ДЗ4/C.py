N = int(input())
matrix = list()
for i in range(N):
    matrix.append(list(map(int, input().split())))

target = 0
result = []

def rec(a,l,N,res:list,count):

    res.append(a)
    l += 1

    for i in range(len(res)):
        if res[i] != res[len(res)-1]:
            count += matrix[len(res)-1][i]

    if l == N:
        global target
        global result
        if count > target:
            target = count
            result = list(res)
        return 0

    for i in range(1,3):
        l_rec = l
        res_rec = list(res)
        count_rec = count
        rec(i,l_rec,N,res_rec,count_rec)

rec(2, l=0, N=N, res=[], count=0)

print(target)
print(*result)