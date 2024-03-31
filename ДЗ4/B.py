N = int(input())
n = [i for i in range(N)]

count = 0

def rec(i,j,l,N,line,column,diag,diag2,n):
    if line & set([i]) or column & set([j]) or diag & set([(j - i)]) or diag2 & set([(j + i)]):
        return 0
    line.add(i)
    column.add(j)
    diag.add(j-i)
    diag2.add(j+i)
    l += 1
    j += 1
    if l == N:
        global count
        count += 1
        return 0
    for num in (set(n)-line):
        l_rec = l
        line_rec = line.copy()
        column_rec = column.copy()
        diag_rec = diag.copy()
        diag2_rec = diag2.copy()
        rec(num,j,l_rec,N,line_rec,column_rec,diag_rec,diag2_rec,n)

for i in range(N):
    line = set()
    column = set()
    diag = set()
    diag2 = set()
    l = 0
    rec(i,0,l,N,line,column,diag,diag2,n)

print(count)