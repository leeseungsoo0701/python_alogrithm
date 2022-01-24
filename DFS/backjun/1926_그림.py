"""
1. 배열의 (0,0)을 입력 값으로 넣는다
2. 거기서부터 입력 값이 1이면 0으로 바꿔주고 이 과정을 for문을 통해 4번 시행한 후 1이 있다면 갯수를 세는 count를 1로 늘려준다, + 전체에 해당하는 count 또한 하나를 늘려준다
3. 위 과정을 반복하여 전체 갯수를 세는 count를 출력하고 해당 블럭의 최댓값을 구하는 Count는 list에 저장후 sort하여 [:-1] 값을 도출한다.

"""
import sys
sys.setrecursionlimit(10**9)


### 행렬 input 받기
N, M = map(int, (input().split()))


k = []
for i in range(0, N):
    k.append(list(map(int, (input().split()))))
# print(k)


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
total_cnt = 0
result = []

def dfs_pic(x, y):
    global total_cnt

    if x < 0 or x >= N or y < 0 or y >= M:
        return False

    if k[x][y] == 1:
        total_cnt += 1
        k[x][y] = 0
        for s in range(4):
            dfs_pic(dx[s] + x, dy[s] + y)
        return True


for n in range(N):
    for m in range(M):
        if dfs_pic(n, m):
            result.append(total_cnt)
            total_cnt = 0



if result:
    print(len(result))
    result.sort()
    print(result[-1])
else:
    print(0)
    print(0)




##################


import sys

sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

count = 0


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        pass

    elif (graph[x][y]):
        graph[x][y] = 0

        global count
        count += 1

        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)

        return 1


result = []

for i in range(n):
    for j in range(m):
        if (dfs(i, j) == 1):
            result.append(count)
            count = 0

if (len(result) == 0):
    print(0)
    print(0)

else:
    print(len(result))
    print(max(result))


