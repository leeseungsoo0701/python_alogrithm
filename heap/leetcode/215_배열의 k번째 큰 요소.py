"""
문제: 정렬되지 않은 배열에서 k번째 큰 요소를 추출하라.

입력: [3,2,3,1,2,4,5,5,6]    k=4
출력 : 4


아이디어:
최대 힙을 만들고
최대값을 추출하는 것을 k번한다.

"""

import heapq

def max_heap(inputs: list[int], k: int) -> int:
    # heap을 먼저 선언한다.
    heap = []

    # heapq를 활용하여 heap 리스트에 n을 힙 형태로 넣어준다.
    for n in inputs:
        heapq.heappush(heap, n)

    # heap이 다 들어갔으면 라스트 형태이므로 reverse 해서 정렬한다.
    sorted_heap = sorted(heap, reverse=True)

    # reverse 된 배열의 인덱스 번호이므로 k-1을 return 해준다.
    return sorted_heap[k - 1]


inputs = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
print(max_heap(inputs, k))



#############################################
# 블로그 풀이
# def findKthLargest(nums: list[int], k: int)-> int:
#     heap = list()

      # heap에 -n을 넣어줘서 큰 값이 가장 작은 값을 만들어 주고 heap에 넣어준다.
#     for n in nums:
#         heapq.heappush(heap, -n)
#
#     ## pop을 heap을 k-1번 해줘서 k번째 수가 가장 앞에 나오도록 지정한다.
#     for _ in range(1, k):
#         heapq.heappop(heap)
#
      # return 할 때 이제 가장 마지막 수를 -를 붙여 원래 수를 나타내도록 한다.
#     return -heapq.heappop(heap)
#
# inputs = [3,2,3,1,2,4,5,5,6]
# k = 4
# print(findKthLargest(inputs,k))


################################################
# 정민님 풀이

# import heapq    # heapq.heappop - 가장 작은 원소 삭제
#
# heap = []
# for val in nums:
#     heapq.heappush(heap, val)

      # 넣어주는데 넣어줄 때 이제 k+1번째 수가 나오면 가장 작은 수부터 pop해준다.
#     if len(heap) > k:
#         heapq.heappop(heap)
#
      # 이 과정을 반복하면 이제 heap 안에는 k개의 가장 큰 값들만 남아있고 그 중에서 가장 작은 값이 k번째 큰 수 이다.
#     return heapq.heappop(heap)
