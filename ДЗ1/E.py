n = int(input())

s = list()

for i in range(n):
    s.append(input())

def radix(A):

    print("Initial array:")
    print(", ".join(A))

    result = []

    i = len(A[0]) - 1 if len(A) > 0 else -1

    while i >= 0:
        print("**********")
        print("Phase " + str(len(A[0]) - i))

        bucket = {"0": [], "1": [], "2": [], "3": [], "4": [], "5": [], "6": [], "7": [], "8": [], "9": []}

        for j in range(len(s)):
            bucket[s[j][i]] += s[j].split()

        for j in range(10):
            if len(bucket[str(j)]) > 0:
                print("Bucket " + str(j) + ": " + ", ".join(bucket[str(j)]))
                result += bucket[str(j)]
            else:
                print("Bucket " + str(j) + ": " + "empty")

        A[:] = result
        result.clear()

        i -= 1

    print("**********")
    print("Sorted array:")
    print(", ".join(A))

    return A

radix(s)