"""
문제 : 널리 잘 알려진 자료구조 중 최소 힙이 있다. 최소 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.

배열에 자연수 x를 넣는다.
배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.
프로그램은 처음에 비어있는 배열에서 시작하게 된다.

입력 :
9
0
12345678
1
2
0
0
0
0
32

출력 :
0
1
2
12345678
0



아이디어:
1. 맨 처음 0이 나올 때의 예외처리
2. 맨 처음이 아니고 0이 나올때에는 이전까지의 값들 중 가장 최소 값을 반환하여 result에 추가 후 heap에는 삭제한다. heappop
3. 위 두 경우가 아닌 경우에는 값을 heappush(heap,num)을 해준다.
4. 전체 입력 받을 수를 먼저 입력 받고 결과에 해당하는 리스트(result)를 따로 생성 , 결과 값을 result에 append한다.
5. return result를 하여 for문을 통해 하나씩 결과가 나오도록 설계한다.
"""
import heapq
import sys
N = int(input())
nums = []
for i in range(N):
    nums.append(int(sys.stdin.readline()))


def min_heap(lists: list[int]):
    heap = []
    result = []
    for idx, num in enumerate(lists):
        if num == 0 and not heap:
            result.append(0)

        if num == 0 and heap:
            result.append(heapq.heappop(heap))

        if num != 0:
            heapq.heappush(heap, num)

    return result


min_heap_list = min_heap(nums)
for heap_num in min_heap_list:
    print(heap_num)
