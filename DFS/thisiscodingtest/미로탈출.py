from collections import deque


#행, 열 입력 받기
N, M = map(int, input().split())

# 그래프 입력 받기 위한 리스트 생성
graph = []


# 입력 받기
for _ in range(N):
    graph.append(list(map(int, input())))


# 상하좌우 방향 리스트
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]



#BFS 함수 생성 파라미터는 초기 위치값
def BFS(x, y):
    # deque 설정
    queue = deque()

    # 초기값 넣어주기
    queue.append((x, y))


    # queue가 존재한다면 아직 내려갈 자식이 있다는 것이다.
    while queue:
        # 부모노드 를 pop하여
        x, y = queue.popleft()

        # 상하좌우로 움직인다.
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            #움직일때 범위 밖이면 그냥 continue로 넘어간다.
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            # 범위 안이지만 괴물 위치라면 넘어간다.
            if graph[nx][ny] == 0:
                continue

            # 만약에 통로라면 부모노드가 가지고 있는 값에 +1을 하여 현재 갈 수 있는 통로에 넣어준다.
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1

                # 현재 지나갈 수 있는 통로들!을 queue에 넣어줘서 다시 돌릴 수 있도록 하게 한다.
                queue.append((nx, ny))

    #함수가 다 끝난다면 배열이므로 전체의 마지막 자식을 꺼낸다면 최소한 이동 칸의 갯수를 val로 가지고 있을 것이므로 위를 return해주면 된다.
    return graph[N - 1][M - 1]


print(BFS(0, 0))
