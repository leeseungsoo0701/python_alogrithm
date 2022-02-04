import sys
import math
from collections import deque

# 남 동 북 서
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, L, R = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

def BFS(x,y)
