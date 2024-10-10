n = int(input())

line = list(map(int, input().split()))

max_dp = line
min_dp = line

for i in range(n-1):
    temp = list(map(int, input().split()))

    max_dp = [temp[0] + max(max_dp[0], max_dp[1]), temp[1] + max(max_dp), temp[2] + max(max_dp[1],max_dp[2])]
    min_dp = [temp[0] + min(min_dp[0], min_dp[1]), temp[1] + min(min_dp), temp[2] + min(min_dp[1],min_dp[2])]

print(max(max_dp), min(min_dp), end=" ")
