"""
문자열 S가 주어질 때, x 혹은 + 를 넣어 만들어질 수 있는 가장 큰수를 구하는 프로그램을 만들어라

"""
from collections import deque


#deque로 설정하여 왼쪽에서부터 하나의 값들을 뽑아내자
nums = deque(input())
result = 0


# 각 숫자를 다 꺼낼때까지 하나의 값 num이 0인지 1인지를 파악하며
# 추가적으로 전체 값이 0일때와 아닐때를 구분해야한다.
# 전체 값이 0이라면 2보다 큰 값이 나오더라도 곱해버리면 0이 되기 때문에 더해줘야한다.
while nums:
    num = int(nums.popleft())
    if result == 0:
        result += num
    else:
        if num == 0 or num == 1:
            result += num
        else:
            result *= num

print(result)
