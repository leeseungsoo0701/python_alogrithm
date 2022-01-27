### BFS

## 아이디어: queue에 다 넣어 하나씩 확인해보는데 지나간 곳은 visitr

from collections import deque


def solution(dirs):
    answer = 0

    # 방문 한 곳 확인하기 위한 이중 배열 완성
    visited = []
    visits = [0 for _ in range(10)]

    ## 이중배열 완성
    for i in range(10):
        visited.append(visits)

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    move_list = deque(dirs)


    def dfs(x, y, answer):

        if x < 0 or x >= 10 or y < 0 or y >= 10:
            return

        visited[x][y] == 1

        while move_list:
            move = move_list.popleft()

            if move == 'U':
                answer += 1
                dfs(x, y + 1, answer)

            elif move == "L" and visited[x + 1][y] and visited[x][y + 1] == 0:
                answer += 1
                dfs(x + 1, y, answer)

            elif move == "R" and visited[x - 1][y] and visited[x][y + 1] == 0:
                answer += 1
                dfs(x - 1, y, answer)

            elif move == "D" and visited[x][y - 1] and visited[x][y - 1] == 0:
                answer += 1
                dfs(x, y - 1, answer)

    dfs(5,5,0)
    return answer

print(solution("ULURRDLLU"))