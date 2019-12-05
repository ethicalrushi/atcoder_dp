n, k = [int(x) for x in input().strip().split()]
a = [int(x) for x in input().strip().split()]

#dp[i][j]: no of ways of distributing j candies among first i children
dp = [[0 for j in range(k+1)] for i in range(n+1)]

for i in range(n+1):
    dp[i][0] = 0

for j in range(k+1):
    dp[0][j]=1

dp[0][0] = 1

for i in range(1,n+1):
    for j in range(1,k+1):
        for m in range(min(a[i-1],j)+1):
            dp[i][j]+=dp[i-1][j-m]

print(dp[n][k])
print(dp)