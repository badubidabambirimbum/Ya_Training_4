t = int(input())

arr = []

for i in range(t):
    arr.append(list(map(int, input().split())))

for j in range(len(arr)):
    if arr[j][1] == arr[j][2]:
        if arr[j][0] % arr[j][1] == 0:
            print("YES")
        else:
            print("NO")
    elif arr[j][0] // arr[j][1] > 1:
        print("YES")
    else:
        print("NO")