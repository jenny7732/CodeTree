# 나머지 나눌 수 
MOD = 10007

NUMBERS = [1,2,5]

n = int(input())

D = [0] * (n+1)

# 선택하지 않았을 경우
# 합 0을 만들기 위한 가짓수는 1
D[0] = 1

for i in range (1,n+1):
    for j in range(3):
        if i >= NUMBERS[j]:
            D[i] = (D[i] + D[i-NUMBERS[j]]) % MOD

print(D[n])