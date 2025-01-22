n, m = map(int, input().split())
A = list(map(int, input().split()))

# 배열 정의 및 초기화
# D는 길이인데 길이가 합보다 클 수 없다. 합(m)이 8이면 아무리 1만 있다고 해도 8을 넘을 수 없다. 
D = [m+10] * (m+10)

D[0] = 0

for j in range(n): #A 배열의 인덱스 느낌
    for i in range(m, -1, -1): #총 합을 거꾸로 찾아가는 느낌
        if A[j] > i :
            continue
        if D[i-A[j]] == m+10: #아직 빈 값이라면 넘어감
            continue
        
        D[i] = min(D[i], (D[i-A[j]]) + 1)

print(D[m] if D[m] != m+10 else -1)
