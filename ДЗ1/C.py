n = int(input())
N = list(map(int, input().split()))

m = int(input())
M = list(map(int, input().split()))

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

print(*merge(M,N))