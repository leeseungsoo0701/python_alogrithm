"""
문제 : 크기가 N인 수열 A = A1, A2, ..., AN이 있다. 수열의 각 원소 Ai에 대해서 오큰수 NGE(i)를 구하려고 한다.
Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다.
그러한 수가 없는 경우에 오큰수는 -1이다.

예를 들어, A = [3, 5, 2, 7]인 경우 NGE(1) = 5, NGE(2) = 7, NGE(3) = 7, NGE(4) = -1이다.
A = [9, 5, 4, 8]인 경우에는 NGE(1) = -1, NGE(2) = 8, NGE(3) = 8, NGE(4) = -1이다.


입력:
4
3 5 2 7

출력 :
5 7 7 -1


아이디어 :
1. 슬라이싱을 통한 max 값 도출
2. 현재 인덱스 값과 비교
3. 현재 인덱스가 더 크면 현재 자리에 -1 , max가 더 크면 max append
4. " ".join(result)
"""
import sys
from collections import deque
num = int(sys.stdin.readline())
nums = list(map(int, input().split()))
stack = []
answer = [-1]*num

for i in range(len(nums)):
    while stack and nums[stack[-1]] < nums[i]:
        answer[stack.pop()] = nums[i]
    stack.append(i)



print(" ".join(map(str,answer)))
