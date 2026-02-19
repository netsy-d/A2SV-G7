matrix = []
for _ in range(5):
    row = list(map(int,input().split()))
    matrix.append(row)
n = len(matrix)
m= len(matrix[0])
for i in range(len(matrix)):
    for j in range(m):
        if matrix[i][j] == 1:
            print(abs(2 - i) + abs(2 - j))
