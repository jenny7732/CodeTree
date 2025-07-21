n = int(input())
nums = list(map(int, input().split()))

count = [0] * 10  # 인덱스 0 ~ 9

for a in nums:
    if 1 <= a <= 9:
        count[a] += 1

for i in range(1, 10):
    print(count[i])
