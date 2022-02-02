import sys
N = int(sys.stdin.readline())

result = []
for _ in range(N):
    num = int(sys.stdin.readline())

    result.append(num)

result.sort()

for i in range(len(result)):
    print(result[i])


