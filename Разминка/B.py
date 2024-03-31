arr = list(map(int , input().split()))

m = 0
n = 0

if arr[1] == arr[3]:
    m = arr[0] + arr[2]
    n = arr[1]
else:
    m = arr[0] * arr[3] + arr[2] * arr[1]
    n = arr[1] * arr[3]

num = min(m,n)

while num != 0 and num != 1:
    if m % num == 0 and n % num == 0:
        m //= num
        n //= num
        num = min(m,n)
    else:
        num -= 1

print(m,n)