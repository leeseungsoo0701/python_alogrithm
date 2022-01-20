import sys
from collections import deque

num = int(sys.stdin.readline())

queue = deque()

while True:
    data = int(sys.stdin.readline())

    if data == -1:
        break

    if data == 0 and queue:
        queue.popleft()
    elif data ==0 and not queue:
        pass
    elif data !=0 and len(queue)< num:
        queue.append(data)

if queue:
    print(" ".join(map(str,queue)))

else:
    print("empty")