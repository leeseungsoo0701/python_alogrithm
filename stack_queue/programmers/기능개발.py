##### 1. 100이 들어있는 progress 길이 만큼의 리스트 만들어주고 거기서 progress를 뺀 다음 speeds로 나눠준 올림값을 queue에 넣는다
##### 2. queue를 while문을 통하여 현재 값이 stack에 쌓인거보다 크면 이제 pop해주고 그 자리에 index 값을 뺴준다
##### 3. 빼준 index값을 answer.appned  return 끝


import math
import collections


def solution(progresses, speeds):
    hun_list = [100] * len(progresses)  ####1

    queue = collections.deque()  ### 뺀 나머지 부분들을 넣는 리스트

    answer = []  ### 결과 담는 리스트

    for i, progress in enumerate(progresses):
        queue.append(math.ceil((hun_list[i] - progresses[i]) / (speeds[i])))  ##올림(100-30/30) = 3

    while queue:
        count = 1
        temp = queue.popleft()  # 맨 처음은 7

        while queue and queue[0] <= temp:
            queue.popleft()
            count += 1

        answer.append(count)

    return answer


progresses = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(progresses, speeds))