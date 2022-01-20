from collections import deque
import sys
num,sib = input().split() ### num과 sib 찾기
node_name = map(int,input().split())
queue = deque(node_name)

while True:
    if num and sib == "0":
        break

    root_node = queue.popleft()


    while queue:







