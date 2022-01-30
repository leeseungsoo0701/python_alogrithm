"""
문자열 S가 주어질 때, x 혹은 + 를 넣어 만들어질 수 있는 가장 큰수를 구하는 프로그램을 만들어라

"""
from collections import deque

nums = deque(input())
result = 0

while nums:
    num = int(nums.popleft())
    if result == 0:
        result += num
    else:
        if num == 0 or num ==1:
            result += num
        else:
            result *= num

print(result)
