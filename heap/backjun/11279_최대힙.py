"""
문제 :
널리 잘 알려진 자료구조 중 최대 힙이 있다. 최대 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.

배열에 자연수 x를 넣는다.
배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.
프로그램은 처음에 비어있는 배열에서 시작하게 된다.

입력 :
13
0
1
2
0
0
3
2
1
0
0
0
0
0

출력 :
0
2
1
3
2
1
0
0
"""

import heapq
import sys

N = int(input())
nums = []

for _ in range(N):
    nums.append(int(sys.stdin.readline()))


def max_heap(nums: list[int]):
    heap = []
    result = []

    ## nums에 해당하는 값들에 있어 판별 후 result에 값을 넣어준다.
    for num in nums:
        if num == 0 and not heap:
            result.append(0)

        # num == 0 이지만 heap이 존재한다면 heap 중에 가장 작은 값을 result에 넣어준다 대신 -를 하여 가장 큰 값으로 해당하도록 넣어준다..
        if num == 0 and heap:
            result.append(-heapq.heappop(heap))

        #num !=0 이 아니라면 push를 마이너스 값을 넣어줘서 가장 큰 값이 가장 작은 값으로 맨 앞에 오도록 설정한다.
        if num != 0:
            heapq.heappush(heap, -num)

    return result


max_heap_list = max_heap(nums)
for heap_num in max_heap_list:
    print(heap_num)
