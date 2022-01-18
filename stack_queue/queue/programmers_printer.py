####### 1. 중요도 높은게 우선
####### 2. 가장 큰거 비교 하고 높은게 있을 시 popleft 하고 append해서 맨 뒤로 붙이자
####### 3. 가장 큰거랑 비교했을 때, temp가 가장 크면 그 값의 index를 proirities의 인덱스 +1 로호출하자.

##########

from collections import deque


def solution(priorities, location):
    answer = 0

    queue = deque()
    # max_priorities = max(priorities)  # 3 고정

    for i, pr in enumerate(priorities):
        queue.append([pr, i])

    print(queue)
    # print(type(max(queue)))

    while queue:
        max_priorities = max(queue)
        print(max_priorities)
        temp = queue.popleft()

        # print(temp[0])    ##### 값 현재는 2
        # print(type(temp))

        if temp[0] < max_priorities[0]:
            queue.append(temp)

        #temp[0] == max_priorities[0]
        else:
            answer += 1
            if temp[1] == location:
                break



        # else:
        #     queue.appendleft(temp)
        #     # if queue[][1] == locaion:
        #     #     answer +=queue.
        #     break

        # if temp[1] == location:
        #     answer += queue.index(temp[0])

    print(queue)

    return answer  ### index 번호


priorities = [2, 1, 3, 2]
location = 2  ## index 번호
print(solution(priorities,location))