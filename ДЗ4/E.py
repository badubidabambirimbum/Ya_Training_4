n = int(input())

def rec(a,l,n,br,st:list,s:str):
    if a == "(":
        st.append(a)
        s += a
    elif a == ")" and len(st) > 0 and st[-1] == "(":
        st.pop()
        s += a
    elif a == "[":
        st.append(a)
        s += a
    elif a == "]" and len(st) > 0 and st[-1] == "[":
        st.pop()
        s += a
    else:
        return 0

    l += 1

    if len(st) > n-l:
        return 0

    if l == n:
        if len(st) == 0:
            print(s)
        return 0

    for b in br:
        l_rec = l
        st_rec = list(st)
        s_rec = str(s)
        rec(b, l_rec, n, br, st_rec, s_rec)

if n != 0:
    br = ["(", "[", ")", "]"]
    stack = []
    s = ""

    rec(br[0], l=0, n=n, br=br, st=stack, s=s)

    br = ["(", "[", ")", "]"]
    stack = []
    s = ""

    rec(br[1], l=0, n=n, br=br, st=stack, s=s)
else:
    print()