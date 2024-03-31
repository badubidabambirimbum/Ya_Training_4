s = list(input())

stek = [""]

for i in range(len(s)):
    if s[i] == ")" and stek[-1] == "(" or s[i] == "]" and stek[-1] == "[" or s[i] == "}" and stek[-1] == "{":
        stek.pop()
    else:
        stek.append(s[i])

if len(stek) == 1:
    print("yes")
else:
    print("no")