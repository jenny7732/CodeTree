nums = [list(map(int, input().split())) for _ in range(4)]

for i in range(4):
    result = 0
    for j in range(4):
        result += nums[i][j]

    print(result)