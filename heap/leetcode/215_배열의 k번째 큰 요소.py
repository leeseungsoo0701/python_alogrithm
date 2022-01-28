"""
문제: 정렬되지 않은 배열에서 k번째 큰 요소를 추출하라.

입력: [3,2,3,1,2,4,5,5,6]    k=4
출력 : 4


아이디어:
최대 힙을 만들고
최대값을 추출하는 것을 k번한다.

"""
import heapq

def max_heap(inputs : list[int], k: int)->int:
    heap = []

    for n in inputs:
        heapq.heappush(heap, n)

    # print(heap)

    sorted_heap = sorted(heap,reverse=True)


    # print(sorted_heap)

    return sorted_heap[k-1]




inputs = [3,2,3,1,2,4,5,5,6]
k = 4
print(max_heap(inputs,k))



#############################################
# def findKthLargest(nums: list[int], k: int)-> int:
#     heap = list()
#     for n in nums:
#         heapq.heappush(heap, -n)
#
#     for _ in range(1, k):
#         heapq.heappop(heap)
#
#     return -heapq.heappop(heap)
#
# inputs = [3,2,3,1,2,4,5,5,6]
# k = 4
# print(findKthLargest(inputs,k))



################################################

# import heapq    # heapq.heappop - 가장 작은 원소 삭제
#
# heap = []
# for val in nums:
#     heapq.heappush(heap, val)
#     if len(heap) > k:
#         heapq.heappop(heap)
#
#     return heapq.heappop(heap)

