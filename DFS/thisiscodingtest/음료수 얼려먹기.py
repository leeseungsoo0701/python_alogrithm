"""
4 5
00110
00011
11111
00000
"""

N, M = 4, 5  # map(int, input().split())

graph = []

for _ in range(N):
    graph.append(list(map(int, input())))

print(graph)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def DFS(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        for j in range(4):
            DFS(x + dx[j], y + dy[j])
        return True

    return False


count = 0
for i in range(N):
    for j in range(M):
        if DFS(i, j):
            count += 1

print(count)
