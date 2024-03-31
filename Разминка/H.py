a = int(input())
b = int(input())
n = int(input())

flag = False

if a > b:
    print("Yes")
else:
    for i in range(n):
        c = b // n
        if b % n != 0:
            c += 1
        if a > c:
            print("Yes")
            flag = True
            break
    if flag == False:
        print("No")