n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

"""
D[i][j] = (i,j)까지 도달했을 때 최대 값
D[i][j] = max(D[i][j-1], D[i-1][j]) + grid[i][j]
"""

#배열 정의
D = [
    [0] * (n+1)
    for _ in range(n+1)
]

# initialize
D[0][0] = grid[0][0]
for i in range (1,n):
    D[i][0] = D[i-1][0] + grid[i][0]
for j in range(1,n):
    D[0][j] = D[0][j-1] + grid[0][j]

# tabulation
for i in range(1, n):
    for j in range(1,n):
        D[i][j] = max(D[i][j-1], D[i-1][j])+grid[i][j]

print(D[n-1][n-1])
