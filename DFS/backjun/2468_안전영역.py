"""
N보다 현재 인덱스의 값이 큰지 안큰지 비교
현재가 작으면 걍 다음껄로 가
현재가 작으면 상하좌우를 비교하고

"""


dx = [0,0,1,-1]
dy = [1,-1,0,0]


def dfs(x,y,h):

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0<=nx<N) and (0<=ny<N):
            if
