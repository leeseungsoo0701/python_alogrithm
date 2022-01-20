import sys
from collections import deque

num = int(sys.stdin.readline())

queue = deque([i+1 for i in range(num)])

answer = deque()

for i in range(num):
    temp = queue.popleft()

    answer.append(temp)
    if queue:
        queue.append(queue.popleft())
    else:
        pass

print(" ".join(map(str,answer)))

