N = int(input())

def rec(n,s: str,l,N):
    if s.find(str(n)) != -1:
        return 0
    s+= str(n)
    l += 1
    if l == N:
        print(s)
        return 0
    for num in range(1,N+1):
        l_rec = l
        s_rec = str(s)
        rec(num,s_rec,l_rec,N)

for num in range(1,N+1):
    s = ""
    l = 0
    rec(num,s,l,N)