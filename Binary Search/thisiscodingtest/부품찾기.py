import sys
from collections import deque


N = int(input())
stack_nums = list(map(int, sys.stdin.readline().split()))

#비교를 하기 위한 정렬
stack_nums.sort()

M = int(input())
know_nums = list(map(int, sys.stdin.readline().split()))

#결과를 담기 위한 리스트
result = []

#맨 앞과 맨 뒤의 인덱스 설정
start = 0
end = len(stack_nums) - 1

#deque를 활용하여 찾고자하는 값을 하나씩 뽑아낸다.
know_queue = deque(know_nums)


def BSearch(stack_nums: list[int], know_nums: list[int]) -> list[str]:
    #글로벌 변수로 가져온다.
    global start
    global end
    # 값이 있으면 yes 문자열로 바꿔줘서 넣어준다.
    res = ''

    #찾고자하는 수의 갯수만큼 for문을 돌린다.
    for _ in range(len(know_nums)):
        #앞에서부터 하나씩 검사한다.
        temp = know_queue.popleft()

        # start와 end를 활용하여 이진 탐색을 진행한다.
        while start <= end:
            mid = (start + end) // 2

            #찾고자 하는 값과 일치한다면 res를 yes로 하고 위 while문을 break한다.
            if temp == stack_nums[mid]:
                res = 'yes'
                break

            # 그게 아니라면 크고 작음에 따라 start와 end 포인트를 옮겨줘서 계속 while문에 들어가도록 한다.
            elif temp < stack_nums[mid]:
                end = mid - 1
            else:
                start = mid + 1

        # 한번의 while문이 돌때동안 start와 end가 변했으므로 초기화시켜준다.
        start = 0
        end = len(stack_nums)-1

        # 한번의 for문 동안은 res가 yes거나 ''일 것이다 위 구분을 져서 result에 바로 문자열로 넣어주자.
        if res == 'yes':
            result.append('yes')
        else:
            result.append('no')
    return

#함수 실행하자
BSearch(stack_nums,know_nums)

# 공백을 기준으로 출력해준다.
print(" ".join(result))