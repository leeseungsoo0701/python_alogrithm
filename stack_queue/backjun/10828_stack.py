from collections import deque
import sys

n = int(sys.stdin.readline())


stack = []

while(n):
    msg = sys.stdin.readline().split()

    if msg[0] == 'push':
        stack.append(msg[1])

    elif msg[0] == 'pop':
        if stack:
            int_pop = stack.pop()
            print(int_pop)
        else:
            print(-1)

    elif msg[0] == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)

    elif msg[0] == 'size':
        if stack:
            print(len(stack))
        else:
            print(0)

    elif msg[0] == "empty":
        if stack:
            print(0)
        else:
            print(1)
    else:
        pass

    n -=1








