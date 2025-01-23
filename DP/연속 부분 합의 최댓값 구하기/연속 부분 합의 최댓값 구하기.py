import sys 

n = int(input())
arr = list(map(int, input().split()))

INT_MIN = -sys.maxsize

# D 배열 정의, 가장 작은 값으로 초기화
D = [INT_MIN] * (n+10)

# 초기 설정
D[0] = arr[0]

# 0은 이미 설정해줬으니 1부터 !
for i in range(1,n):
    D[i] = max(D[i-1]+arr[i], arr[i])

print(max(*D))

