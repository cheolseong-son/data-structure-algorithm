# 1로 만들기
# https://www.acmicpc.net/problem/1463

n = int(input())
#  탑-다운 방식
dp = [0] * (n+1)  # 값을 저장할 DP

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    # 2로 나누어 질 때
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    # 3으로 나누어 질 때
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[n])
