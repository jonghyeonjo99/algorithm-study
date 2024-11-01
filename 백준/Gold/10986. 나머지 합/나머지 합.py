n, m = map(int, input().split())
number = list(map(int, input().split()))

dp = [0 for _ in range(n)]
dp[0] = number[0]
for i in range(1, n):
    dp[i] = dp[i-1] + number[i]

# print(dp)
count = 0
rest = [0 for _ in range(m)]
for i in range(n):
    rest[dp[i] % m] += 1
    if dp[i] % m == 0:
        count += 1

for i in rest:
    if i >= 2:
        count += i * (i - 1) // 2

print(count)