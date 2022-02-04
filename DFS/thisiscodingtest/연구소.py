import copy

N, M  = map(int, input().split())
wall = 3
graph = []


# 입력 받기
for _ in range(N):
    graph.append(list(map(int, input().split())))


cp_graph = copy.deepcopy(graph)


# print(graph)

