"""
볼링공 고르기

5 3
1 3 2 3 2

8 5
1 5 4 3 2 4 5 2
"""
#N, M 입력 받기
N, M = map(int, input().split())

# 공의 무게 입력 받기
ball_list = list(map(int, input().split()))
#결과값에 대한 변수 생성하기
count = 0

# 이중 for문을 통한 현재 값과 현재 값을 제외한 모든 뒤의 값들에 대한 비교 및 count 추가.
for i in range(N):
    for j in range(i + 1, N):
        if ball_list[i] == ball_list[j]:
            continue
        else:
            count += 1

print(count)

##########################################################
from collections import deque

#N, M 입력 받기
N, M = map(int, input().split())

# 공의 무게 입력 받기
ball_list = list(map(int, input().split()))

#deque로 만들어주기
ball_list = deque(ball_list)

#결과값에 대한 변수 생성하기
count = 0

# queue를 활용하여 하나씩 빼주기
while ball_list:
    #가장 왼쪽 값을 빼고
    temp = ball_list.popleft()

    # 그 값이 남은 ball_list에 없다면 전체를 다 더해줘야하므로
    if temp not in ball_list:

        # len길이를 count에 더해준다
        count += len(ball_list)
        continue

    #ball_list에 남아 있다면 temp 값에 해당하는 갯수를 전체 len에서 빼준 값을 count에 더해준다.
    else:
        count += len(ball_list) - ball_list.count(temp)

print(count)


