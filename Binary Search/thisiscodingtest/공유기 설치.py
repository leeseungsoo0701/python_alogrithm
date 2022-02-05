"""
5 3
1
2
8
4
9
"""


N, C = map(int,input().split())

result = []

for _ in range(N):
    result.append(int(input()))

result.sort()

min_num = result[0]
max_num = result[-1]

len_result = max_num-min_num

title = round(len_result/C)

print(title)
