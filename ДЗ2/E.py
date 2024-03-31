s = input()

nums = ""

for i in range(len(s)-1):
    nums += s[i] + "$"
nums += s[-1]

numsr = ""
numsr = nums[::-1]

def hash_table(s, p, x_, x):
    table = [0] * (len(s) + 1)

    for i in range(1, len(table)):
        table[i] = (table[i - 1] * x_ + ord(s[i - 1])) % p
        x[i] = (x[i - 1] * x_) % p
    return table


def equality(l, a, b, table, table_r, x, p):
    if (table_r[l + a] - table_r[a] * x[l]) % p == (table[l + b] - table[b] * x[l]) % p:
        return True
    else:
        return False


x = [1] * (len(nums) + 1)
p = (10 ** 9) + 7

h1 = hash_table(nums, p, 257, x)
h2 = hash_table(numsr, p, 257, x)

result = 0

for i in range(len(nums)):
    if i <= len(nums) // 2:
        l = 0
        r = i + i
    else:
        r = len(nums) - 1
        l = r - (r - i) * 2

    if equality(r-l+1, len(h2)-(r+1)-1, l, h1, h2, x, p):
        if nums[i] == "$":
            if (r - i) % 2 != 0:
                result += (r-l) // 4 + 1
            else:
                result += (r-l) // 4
        else:
            if (r - i) % 2 != 0:
                result += (r-l) // 4 + 1
            else:
                result += (r-l) // 4 + 1
    else:
        target = 0
        lf = i
        rf = r
        while rf - lf > 1:
            mid = (rf+lf) // 2
            l = i - (mid-i)

            if equality(mid - l + 1, len(h2) - (mid + 1) - 1, l, h1, h2, x, p):
                if nums[i] == "$":
                    if (mid - i) % 2 != 0:
                        target = (mid - l) // 4 + 1
                    else:
                        target = (mid - l) // 4
                else:
                    if (mid - i) % 2 != 0:
                        target = (mid - l) // 4 + 1
                    else:
                        target = (mid - l) // 4 + 1

                lf = mid

            else:
                rf = mid

        result += target

print(result)