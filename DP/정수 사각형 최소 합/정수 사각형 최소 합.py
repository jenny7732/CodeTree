n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# 배열 정의
D = [
    [0] * (n+1)
    for _ in range(n+1)
]

# 배열 초기화
D[0][n-1] = grid[0][n-1]

# 열 초기화 
for i in range(1,n):
    D[i][n-1] = D[i-1][n-1] + grid[i][n-1]

# 행 초기화
for i in range(n-2, -1, -1):
    D[0][i] = D[0][i+1] + grid[0][i]
   
for i in range(1,n):
    for j in range(n-2, -1, -1):
        D[i][j] = min(D[i-1][j], D[i][j+1]) + grid[i][j]

print(D[n-1][0])
    

