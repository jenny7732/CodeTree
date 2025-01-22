n = int(input())
a = list(map(int, input().split()))

D = [0] * (n)

for i in range(n):
    D[i] = 1

for i in range(n):
    for j in range(i):
        if(a[j] > a[i]):
            D[i] = max(D[i], (D[j] + 1))

print(max(D))