import sys
from collections import deque

N = int(sys.stdin.readline())
graph = []

# 각 집으로의 이동을 표현할 좌표리스트
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(N):
    graph.append(list(map(int, input())))

count = 0

def bfs(x, y):
    # 함수 내에서 개별 단지의 집 개수를 세줄 변수
    global count
    q = deque()
    q.append((x, y))

    # 처음으로 방문한 곳에 대해 방문 처리
    graph[x][y] = 0

    while q:
        x, y = q.popleft()
        count += 1  # 결국엔 q에 들어가는 수와 각 단지의 집의 개수는 같기 때문에 여기서 count += 1 해준다

        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y

            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0

                q.append((nx, ny))

    return count  # 모두 방문한 후에는 count를 리턴

# 전체 단지 갯수
total = 0

# 개별 단지의 집 갯수를 담아줄 리스트
nums_list = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            nums_list.append(bfs(i, j))
            total += 1  # bfs를 1회 진행하고 나면 한 단지 내의 모든 집에 대한 방문이 끝남

print(total)
for x in sorted(nums_list):
    print(x)