n = int(input())
arr = list(map(int , input().split()))

result = [0] * n
sm1 = sum(arr)
sm2 = 0

for i in range(len(arr)):
    result[i] = (sm1 - (len(arr)-i) * arr[i]) + (abs(sm2 - i * arr[i]))
    sm1 -= arr[i]
    sm2 += arr[i]

print(*result)