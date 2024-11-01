n, m = map(int, input().split())
number = list(map(int, input().split()))

dp = [0 for _ in range(n)]

dp[0] = number[0]
for i in range(1,n):
    dp[i] = dp[i-1] + number[i]

# print(dp)

for i in range(m):
    a,b = map(int, input().split())
    if a != 1:
        result = dp[b-1] - dp[a-2]
    else:
        result = dp[b-1]
    print(result)