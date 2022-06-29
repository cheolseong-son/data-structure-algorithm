# https://www.acmicpc.net/problem/2644
from sys import stdin
from collections import deque

input = stdin.readline  # 입력값 받기

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]  # 2차원 리스트 생성
visited = [0 for _ in range(n+1)]  # 방문처리를 위한 리스트

# 그래프 생성(양방향)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = 1
    while queue:
        node = queue.popleft()

        for i in graph[node]:
            if visited[i] == 0:
                visited[i] += (visited[node] + 1)
                queue.append(i)


bfs(a)

if visited[b] != 0:
    print(visited[b]-1)
else:
    print(-1)
