# n층 최대 높이
MAX_N = 1000

# 나머지 나눌 수
MOD = 10007

# 변수 입력 및 선언
n = int(input())
D = [0] * (MAX_N +1)

# 초기 조건 설정
D[0] = 1
D[1] = 0
D[2] = 1
D[3] = 1

for i in range(4, n+1):
    D[i] = (D[i-2] + D[i-3]) % MOD

print(D[n])

