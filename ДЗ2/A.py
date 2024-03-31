s = input()
n = int(input())

nums = list()

for i in range(n):
    nums.append(list(map(int, input().split())))

def hash_table(s, p, x_, x):
    table = [0] * (len(s) + 1)

    for i in range(1, len(table)):
        table[i] = (table[i - 1] * x_ + ord(s[i - 1])) % p
        x[i] = (x[i - 1] * x_) % p
    return table

def equality(l, a, b, table, x, p):

    if (table[l + a] - table[a] * x[l]) % p == (table[l + b] - table[b] * x[l]) % p:
        print("yes")
    else:
        print("no")


x = [1] * (len(s) + 1)
p = (10 ** 9) + 7

table = hash_table(s, p, 257, x)

for i in range(len(nums)):
    equality(nums[i][0], nums[i][1], nums[i][2], table, x, p)