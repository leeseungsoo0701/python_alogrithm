"""
p.110

"""

from collections import deque

# 입력받을 명령의 수
N = int(input())

# list형의 str 명령을 받도록 하자
orders = list(map(str, input().split()))

# 초기값 세팅
x, y = 1, 1

# 명령을 dic형태로 만들어 value로는 tuple 형태로 작성한다.
dic = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}


# orders에 존재하는 order에 대하여
for order in orders:

    # 그 값을 먼저 추출한다
    (nx, ny) = dic[order]

    # 만약 범위 안에 존재한다면 변화한 곳의 위치를 현재 위치에 넣어준다.
    if 1 <= x+nx <= N and 1 <= y+ny <= N:
        x, y = nx+x, ny+y
        nx, ny = x, y


# 최종 위치를 출력한다.
print(x, y)
