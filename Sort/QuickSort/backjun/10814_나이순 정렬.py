import sys

N = int(sys.stdin.readline())


result = []
for count in range(N):
    data = list(map(str,input().split()))
    result.append((int(data[0]),data[1],count))

result = sorted(result, key=lambda sorted_age:(sorted_age[0],sorted_age[2]))

for i in range(N):
    print(str(result[i][0])+ ' ' + result[i][1])