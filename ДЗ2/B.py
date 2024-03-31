s = input()
result = len(s)

def hash_table(s, p, x_, x):
    table = [0] * (len(s) + 1)

    for i in range(1, len(table)):
        table[i] = (table[i - 1] * x_ + ord(s[i - 1])) % p
        x[i] = (x[i - 1] * x_) % p
    return table


def equality(l, a, b, table, x, p):

    if (table[l + a] - table[a] * x[l]) % p == (table[l + b] - table[b] * x[l]) % p:
        return True
    else:
        return False


x = [1] * (len(s) + 1)
p = (10 ** 9) + 7


table = hash_table(s, p, 257, x)

for i in range(1, len(s)):
    if equality(len(s) - i, 0, 0 + i, table, x, p) and i < result:
        result = i
        break

print(result)