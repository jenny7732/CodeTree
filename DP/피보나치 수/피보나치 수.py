N = int(input())

F = [0] * 48

F[1] = 1
F[2] = 1

for i in range (3,N+1):
    F[i] = F[i-1]+F[i-2]

print(F[N])


