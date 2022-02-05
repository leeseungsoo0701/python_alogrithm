"""
3 3
1 0 2
0 0 0
3 0 0
2 3 2
"""
from collections import deque

# N,K 입력 받기
N, K = map(int, input().split())

#그래프 입력 받기 위한 리스트 생성
graph = []

# 바이러스 위치의 입력을 받기 위한 리스트 생성
result = []

# 입력 받기
for i in range(N):
    graph.append(list(map(int, input().split())))

    #0이 아니라면 바이러스이므로 (1,1)부터 시작이므로 i와 j에 +1씩 해줘서 가독성 좋게 넣어주자
    for j in range(N):
        if graph[i][j]:
            result.append((i + 1, j + 1, graph[i][j], 0))

# 바이러스의 숫자 기준으로 정렬해준다.
result.sort(key=lambda x: x[2])


# print(result)

# S,X,Y
S, X, Y = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

#BFS로 풀이한다 왜? 1,2,3이 한번에 옮겨져야하므로
def BFS(S: int, X: int, Y: int) -> int:
    queue = deque(result)

    while queue:
        # 하나씩 다 뽑고
        x, y, virus, time = queue.popleft()

        #가독성을 위해 더해주었던 값들을 하나씩 빼준다(인덱스에 넣어줘야하므로)
        x = x - 1
        y = y - 1

        #만약 time을 뒤에 넣어줄텐데 S와 같다면 위의 while문을 break하면 된다.
        if time == S:
            break

        #4방향으로 다 돌려야하고 만약에 범위 내에 없다면 continue
        for t in range(4):
            nx = x + dx[t]
            ny = y + dy[t]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            # 범위 내에 있는데 움직인 방향에서 0이 있다면 virus값을 넣어주고 그 방향에 대해서 다시 queue에 넣어준다.
            else:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = virus
                    queue.append((nx, ny, virus, time + 1))

    #마지막에는 다 움직여졌을 것이므로 입력 값 X-1,Y-1에 대해서 return 해주면 그 값이 return 된다.
    return graph[X - 1][Y - 1]


print(BFS(S, X, Y))
