from collections import deque
import sys

n = int(sys.stdin.readline())


queue = deque()

while (n>0):
    msg = sys.stdin.readline().split()

    if msg[0] == 'push':
        queue.append(msg[1])

    elif msg[0] == 'pop':
        if queue:
            int_pop = queue.popleft()
            print(int_pop)
        else:
            print(-1)

    # elif msg[0] == "top":
    #     if queue:
    #         print(queue[-1])
    #     else:
    #         print(-1)

    elif msg[0] == 'size':
        if queue:
            print(len(queue))
        else:
            print(0)

    elif msg[0] == "empty":
        if queue:
            print(0)
        else:
            print(1)

    elif msg[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)

    elif msg[0] == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)
    else:
        pass

    n -=1








