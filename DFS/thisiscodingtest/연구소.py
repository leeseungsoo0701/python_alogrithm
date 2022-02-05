"""
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

"""

import copy

N, M = map(int, input().split())
wall = 3
graph = []

# 입력 받기
for _ in range(N):
    graph.append(list(map(int, input().split())))



dx, dy = [1,0,-1,0], [0,1,0,-1]

answer = 0


def make_wall(wall_num):
    if wall_num == 3:
        start_virus(copy.deepcopy(graph))

    for i in range(N*M):
        if graph[i // M][i % M]: continue




