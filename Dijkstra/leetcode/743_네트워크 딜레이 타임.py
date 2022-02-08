"""
K부터 출발해 모든 노드가 신호를 받을 수 있는 시간을 계산하라. 불가능할 경우 -1을 리턴한다. 입력값(u,v,w)는 각각 출발지,도착지,소요 시간으로 구성되며, 전체 노드의 개수는 N으로 입력받는다.

입력 : times= = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2

출력 : 2

"""
import heapq
from collections import defaultdict

N, K = 4, 2
times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]


def NetworkDelay(times: list[list[int]], N: int, K: int) -> int:
    # 인자로 주어진 객체의 기본값을 딕셔너리의 초깃값을 지정할 수 있기에 사용
    graph = defaultdict(list)

    # defaultdict(list)를 해줬기에 start_node를 키 값으로
    # (end_node,start_to_end_time)을 튜플 형태로 리스트에 append한다.
    for startNode, endNode, start_to_end_time in times:
        graph[startNode].append((endNode, start_to_end_time))

    # Q를 넣어주기 위한 초기값으로 길이와 시작 노드를 튜플 형태로 리스트에 하나 넣어준다.
    Q = [(0, K)]

    # 거리에 대해서도 객체의 기본값을 딕셔너리의 초깃값을 지정할 수 있기에 사용
    dist = defaultdict(int)

    while Q:
        startNode_to_currNode_time, currNode = heapq.heappop(Q)

        # 한 번도 방문한 적이 없다면 지금 방문하는 순간이 무조건 최소값이다.
        # 왜? -> heapq를 사용했기에 거리가 짧은 순으로 정렬되며 도착노드를
        # 처음 방문 시의 값이 가장 최솟값이라고 자명하게 말할 수 있다.
        # 방문한 적이 없다면 딕셔너리 형태로 현재 노드까지의 시간을 넣어준다.
        if currNode not in dist:
            dist[currNode] = startNode_to_currNode_time    # <= startNode_to_endNode_time

            # 현재 노드에서 연결된 모든 자식 노드들을 보자.
            # 현재 노드에서 자식 노드로 가는 노드와, 자식 노드까지의 거리를 꺼내서
            for currNode_to_endNode, currNode_to_endNode_time in graph[currNode]:
                # 시작 노드에서 최종 자식 노드로 가는 시간 = 시작 노드에서 현재 노드까지의 걸린 시간 + 현재 노드에서 자식 노드까지 걸리는 시간
                startNode_to_endNode_time = startNode_to_currNode_time + currNode_to_endNode_time

                # 이제 자식 노드와 시작노드에서 최종 자식노드까지의 거리를 다시 heapq에 넣어준다면 길이가 짧은 순으로
                # 상단에서 pop되기에 각 노드까지의 거리들 중 최소 길이만으로 갱신이 가능하다.
                heapq.heappush(Q, (startNode_to_endNode_time, currNode_to_endNode))

    # while이 다 끝난 후 딕셔너리에 해당하는 키값이 N개라면
    # 즉 모든 노드들을 다 거쳐 키값을 만들어 냈다면
    if len(dist) == N:

        # 딕셔너리의 value들 즉 시작노드에서의 거리값 중 최댓값을 return한다.
        return max(dist.values())

    # 아닌 경우는 그냥 -1을 return 한다.
    return -1


print(NetworkDelay(times, N, K))

