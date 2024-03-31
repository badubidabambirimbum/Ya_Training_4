nm = list(map(int, input().split()))

matrix = []

for i in range(nm[0]):
    matrix.append(list(map(int, input().split())))

target = 0

for i in range(nm[0]):
    for j in range(nm[1]):
        if matrix[i][j] == 1 and target == 0:
            target = 1
        if matrix[i][j] == 1 and i > 0 and j > 0 and matrix[i-1][j] > 0 and matrix[i][j-1] > 0 and matrix[i-1][j-1] > 0:
            matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1])
            if matrix[i][j] - matrix[i-1][j-1] <= 0:
                matrix[i][j] += 1
            if matrix[i][j] > target:
                target = matrix[i][j]

print(target)