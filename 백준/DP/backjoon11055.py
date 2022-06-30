# 가장 큰 증가 부분 수열
# https://www.acmicpc.net/problem/11055

from copy import deepcopy

N = int(input())
li = list(map(int, input().split()))
dp = deepcopy(li)

for i in range(1, N):
    for j in range(i):
        if li[j] < li[i]:
            dp[i] = max(dp[i], li[i]+dp[j])
print(max(dp))
