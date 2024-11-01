n, k = map(int, input().split())
temperature = list(map(int, input().split()))

dp = [0 for _ in range(n)]
dp[0] = temperature[0]
for i in range(1, n):
    dp[i] = dp[i-1] + temperature[i]

answer = dp[k-1]
for i in range(k, n):
    answer = max(answer, dp[i] - dp[i-k])

print(answer)