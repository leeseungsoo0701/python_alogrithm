from collections import deque
import sys

n = int(sys.stdin.readline())
stack = []
result = []
count = 0
msg = True

for i in range(n):
    num = int(sys.stdin.readline())   #### 4 3

    while count < num:
        count +=1
        stack.append(count)
        result.append("+")

    if stack[-1] == num :
        stack.pop()
        result.append("-")

    else:
        msg =False

if msg ==False:
    print("NO")
else:
    print("\n".join(result))