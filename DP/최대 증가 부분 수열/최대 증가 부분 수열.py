n = int(input())
a = list(map(int, input().split()))

"""
D[i] : i번째 위치를 마지막으로 하는 최대증가부분수열의 길이
D[i] : max(D[j]+1) if j<i and a[j]<a[i]
"""

# 배열 정의
D = [0] * (n+1)

# initialize
for i in range(n):
    D[i] = 1

# tabulation
for i in range(1, n):
    for j in range(i):
        if a[j] < a[i]:
            D[i] = max(D[i], D[j]+1)

# for문 돌려서 D배열 전체에서 Max 값 찾는다는 뜻과 동일
print(max(*D))
