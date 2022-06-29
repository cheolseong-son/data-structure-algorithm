n = int(input())
m = int(input())
INF = int(1e9)

graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신의 비용을 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

# 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n+1):
    count = 0
    for j in range(1, n+1):
        if graph[i][j] == INF and graph[j][i] == INF:
            count += 1
    print(count)
