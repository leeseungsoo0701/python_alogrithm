import sys

N = int(sys.stdin.readline())

result = []
for count in range(N):
    age, name = map(str, input().split())
    result.append((age,name,count))

result = sorted(result, key=lambda sorted_age:(sorted_age[0],sorted_age[2]))

for i in range(N):
    print(result[i][0]+ ' ' + result[i][1])