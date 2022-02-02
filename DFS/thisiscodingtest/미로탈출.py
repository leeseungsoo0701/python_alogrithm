from collections import deque

N, M = 5, 6  # map(int, input().split())

graph = []

for _ in range(N):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

queue = deque()
count = 1

def BFS(x, y):
    global count
    if x < 0 or x >= N or y < 0 or y >= M:
        return False

    if graph[x][y] == 0:
        pass ##????

    if graph[x][y] == 1:


    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            BFS(x + dx[i], y + dy[i])
