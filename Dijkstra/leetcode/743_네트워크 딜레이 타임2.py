from prometheus_client.utils import INF
import heapq


N, K = 4, 2
times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]


def NetworkDelay(times: list[list[int]], N: int, K: int) -> int:
    # 출발, 도착, 시간을 입력받기 위한 이중배열 생성(여기서 중요한 점은 시작은 0번째 노드이므로
    # N+1번째까지 만들어준 뒤 마지막에 [1:]로 슬라이싱한다.)
    graph = [[] for _ in range(N + 1)]

    # 거리도 마찬가지로 N+1만큼 만들어주고 INF로 초기화 시켜준다.
    dist = [INF] * (N + 1)

    # graph에 시작점이 인덱스이고 (도착노드,길이)가 튜플형태로 value로 추가한다.
    for i in times:
        graph[i[0]].append((i[1], i[2]))

    # Q를 하나의 리스트로 value는 튜플형태로 만들어주어 처음 시간값과 출발 위치를 넣어준다.
    Q = [(0, K)]

    # 출발하는 지점에서의 시간는 INF -> 0으로 초기화 해줘야한다.
    # (자기 자신의 노드를 방문하지 않기 때문에 0으로 지정)
    dist[K] = 0


    #Q가 존재할 때까지 while문을 실행한다.
    while Q:
        # 들어온 값들에 대하여 가장 시간이 작은 원소를 기준으로 시간와 현재 노드 위치를 pop 해준다.
        time, curr = heapq.heappop(Q)

        # 시작 노드에서 현재 노드까지의 걸리는 시간이
        # 새로 갱신된 현재 노드까지의 시간와 비교하였을 때,
        # 새로 갱신된 시간가 현재 존재하는 최소 시간보다 길다면 pass
        if dist[curr] < time:
            continue

        # 현재 노드에서 연결되어 있는 모든 자식 노드들을 탐색
        for adj, d in graph[curr]:

            # 시작노드에서 자식노드까지 가는 시간 = 현재 노드까지 왔던 시간 + 현재 노드에서 다음 자식 노드까지 가는 시간
            cost = time + d

            # 더한 시간(cost)는 이전의 시작노드에서 최종 자식 노드까지의 거리와 비교한다. 더한 거리가 작다면 다시 새로 갱신한다.
            if cost < dist[adj]:
                dist[adj] = cost

                # 마지막으로 다음으로 향하는 노드와 지금까지 더한 길이를 heapq에 다시 넣어준다.
                heapq.heappush(Q, (cost, adj))

    # 처음에 설명하였듯이 0부터가 아닌 1부터로 설정해야한다. 그 중 가장 큰 값을 result라는 변수에 넣어준다.
    result = max(dist[1:])

    # 가장 큰 값이 INF라는 것은 아직 방문 못한 node가 있다는 뜻이므로 있으면 -1 아니면 최댓값인 result를 return한다.
    if result != INF:
        return result
    else:
        return -1


print(NetworkDelay(times, N, K))
