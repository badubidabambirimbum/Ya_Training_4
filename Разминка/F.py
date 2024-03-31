k = int(input())
n = int(input())

lift = []

for i in range(n):
    lift.append(int(input()))

result = 0
target = k
counter = -1

i = len(lift) - 1
while i >= 0:

    result += (i + 1) * 2 * (lift[i] // k)

    lift[i] -= (lift[i] // k) * k

    if target == k and lift[i] != 0:
        counter = i

    if lift[i] <= target:
        target -= lift[i]
        lift[i] = 0
    elif lift[i] > target:
        lift[i] -= target
        target = 0

    if target == 0:
        result += (counter+1) * 2
        target = k
        counter = -1
    if lift[i] == 0:
        i -= 1

if counter > -1:
    result += (counter+1) * 2

print(result)