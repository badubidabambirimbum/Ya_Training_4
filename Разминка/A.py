m = list(map(int , input().split()))
arr = list(map(int , input().split()))
n = list()
for i in range(m[1]):
	n.append(list(map(int , input().split())))

counter = 0

for i in range(len(n)):
    l = n[i][0]
    r = n[i][1]
    target = arr[l]
    while l < r:
        l += 1
        if arr[l] < target:
            counter += 1
            print(target)
            break
        elif arr[l] != target:
            counter += 1
            print(arr[l])
            break
    if counter == 0:
        print("NOT FOUND")
    else:
        counter = 0