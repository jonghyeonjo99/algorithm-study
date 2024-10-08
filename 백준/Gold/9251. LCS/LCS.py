
string_a = input()
string_b = input()

dp = [[0 for _ in range(len(string_b) + 1)] for _ in range(len(string_a) + 1)]

for i in range(1, len(string_a) + 1):
    for j in range(1, len(string_b) + 1):
        if string_a[i-1] == string_b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])