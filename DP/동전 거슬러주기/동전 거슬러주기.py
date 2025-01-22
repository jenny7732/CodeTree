N, M = map(int, input().split())
coin = list(map(int, input().split()))

"""
D[i]: i만큼의 금액을 만들 때 사용되는 최소 동전 수
D[i]= min(D[i-coin[j]] + 1)
i >= coin[j]
D[i-coin[j]] 갱신된 값인지
"""
# 배열 정의
D = [0]*(M+1)

#initial
for i in range(1, M+1):
    D[i] = M+10 

#tabulation
for i in range(1, M+1):
    for j in range(N):
        if i < coin[j]:
            continue
        if D[i-coin[j]] == M+10:
            continue
        D[i] = min(D[i], D[i-coin[j]] +1)

print(D[M] if D[M]!=M+10 else -1)
