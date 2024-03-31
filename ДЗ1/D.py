n = int(input())
N = list(map(int, input().split())) if n > 0 else list()

def merge(M,N):

    m = 0
    n = 0
    MN = list()

    while m < len(M) and n < len(N):

        if M[m] <= N[n]:
            MN.append(M[m])
            m += 1
        elif M[m] > N[n]:
            MN.append(N[n])
            n += 1

    if m < len(M):
        MN.extend(M[m-len(M):])
    elif n < len(N):
        MN.extend(N[n-len(N):])

    return MN

def sort_merge(N):
    if len(N) == 1 or len(N) == 0:
        return N
    p = len(N) // 2
    l = sort_merge(N[:p])
    r = sort_merge(N[p:])
    mid = merge(l,r)
    return mid

print(*sort_merge(N))