"""
K부터 출발해 모든 노드가 신호를 받을 수 있는 시간을 계산하라. 불가능할 경우 -1을 리턴한다. 입력값(u,v,w)는 각각 출발지,도착지,소요 시간으로 구성되며, 전체 노드의 개수는 N으로 입력받는다.

입력 : times= = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2

출력 : 2

"""
import heapq
from collections import defaultdict
# N, K = 4, 2
# times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
#
#
#
#
# def NetworkDelay(times:list[list[int]],N:int,K:int)->int:
#     graph = defaultdict(list)
#
#     for start,end,time in times:
#         graph[start].append((end,time))
#
#     Q = [(0,K)]
#
#     dist = defaultdict(int)
#
#     while Q:
#         time, node = heapq.heappop(Q)
#         if node not in dist:
#             dist[node] = time
#             for end_, time_ in graph[node]:
#                 alt = time + time_
#                 heapq.heappush(Q,(alt,end_))
#                 print(Q)
#
#     if len(dist) == N:
#         return max(dist.values())
#
#     return -1
#
# print(NetworkDelay(times,N,K))

####################################################################################
from prometheus_client.utils import INF
import heapq
from collections import defaultdict

N, K = 4, 2
times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]


def NetworkDelay(times: list[list[int]], N: int, K: int) -> int:
    # 출발, 도착, 시간을 입력받기 위한 이중배열 생성(여기서 중요한 점은 시작은 0번째 노드이므로
    # N+1번째까지 만들어준 뒤 마지막에 [1:]로 슬라이싱한다.)
    graph = [[] for _ in range(N + 1)]

    #거리도 마찬가지로 N+1만큼 만들어주고 INF로 초기화 시켜준다.(값을 줄일때는 INF, 최댓값을 자꾸 늘려야할 때는 -INF일 것이다.)
    dist = [INF] * (N + 1)

    # 입력 받은 이중 배열에 있어 미리 빈 이중 리스트로 만들어준 graph에 시작점이 인덱스이고 (도착지점,길이)가 튜플형태로 value로 추가한다.
    for i in times:
        graph[i[0]].append((i[1], i[2]))

    # Q를 하나의 리스트의 튜플형태로 만들어주어 처음 길이값과 출발 위치를 넣어준다.
    Q = [(0, K)]

    #출발하는 지점에서의 길이는 INF -> 0으로 초기화해줘야한다.(자기 자신의 노드를 방문하지 않기 때문에)
    dist[K] = 0

    #BFS형태와 비슷하게 Q가 존재할 때까지 while문을 실행한다.
    while Q:
        # 들어온 값들에 대하여 가장 길이가 작은 원소를 기준으로 길이와 현재 위치를 pop 해준다.
        time, curr = heapq.heappop(Q)

        # 시작노드에서 현재 노드까지의 걸리는 시간이 새로 갱신된 도착 노드까지의 거리와 비교하였을 때,
        # 새로 갱신된 길이가 현재 존재하는 최소 길이보다 길다면 pass
        if dist[curr] < time:
            continue

        # 현재 노드에서 연결되어 있는 모든 노드들을 탐색
        for adj, d in graph[curr]:

            #현재 노드까지 왔던 거리 + 현재 노드에서 다음 노드까지 가는 거리
            cost = time + d

            #더한 거리(cost)는 이제 현재 노드에서 83번째줄의 다음 노드까지의 거리와 비교한다. 더한 거리가 작다면 다시 새로 갱신한다.
            if cost < dist[adj]:
                dist[adj] = cost

                #마지막으로 다음으로 향하는 노드와 지금까지 더한 길이를 heapq에 다시 넣어준다.
                heapq.heappush(Q, (cost, adj))

    #처음에 설명하였듯이 0부터가 아닌 1부터로 설정해야한다. 그 중 가장 큰 값을 result라는 변수에 넣어준다.
    result = max(dist[1:])

    # 가장 큰 값이 INF라는 것은 아직 방문 못한 node가 있다는 뜻이므로 있으면 -1 아니면 최댓값인 result를 return한다.
    if result != INF:
        return result
    else:
        return -1


print(NetworkDelay(times, N, K))
