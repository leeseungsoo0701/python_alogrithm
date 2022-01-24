N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
result = []

def dfs_recursie(node, visited):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    rows, cols = N , N
    count = 0

    for row in range(rows):
        for col in range(cols):
            if arr[row][col] != '1':
                continue

            count += 1

            stack = [(row,col)]

            while stack:
                x, y = stack.pop()
                arr[x][y] = '0'
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if nx < 0 or nx >=rows or ny>=cols or arr[nx][ny] != '1':
                        continue
                    stack.append((nx,ny))
        return count