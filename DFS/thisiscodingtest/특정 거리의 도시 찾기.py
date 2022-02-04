from collections import deque , defaultdict

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
city_num, road_num, distance, start_city = map(int, input().split())

# 출발과 도착이 있고 출발이 겹치는 경우가 있기에 key는 시작 점, value는 리스트로 도착점들을 추가한다.
graph = dict()

# 모든 도로 정보 입력 받기
for _ in range(road_num):
    start, end = map(int, input().split())

    #이미 키 값이 존재한다면 리스트로 붙여주기
    if start in graph.keys():
        graph[start].append(end)    # {"1", [2,3], "2",[3,4]}

    # 없다면 추가해주기
    else:
        graph[start] = [end]


# 필요한 것은 graph와 초기 값이다.
def bfs(graph, start):

    #deque로 만들어주고 우선 start 지점을 queue에 넣어준다.
    que = deque()
    que.append(start)

    # 방문한 도시에 대한 길이를 우선 -1로 설정해준다음
    distance_list = [-1] * (city_num+1)

    #출발 지점만 0으로 바꿔준다. [-1,-1,-1,....0,-1,-1,-1,...]
    distance_list[start] = 0

    #queue가 존재할때까지 즉, 모든 경로를 다 지나갈때까지
    while que:
        front = que.popleft()

        #넣어준 값들이 만약에 키 값에 없다면 그냥 넘어간다.
        if front not in graph:
            continue
        # 키 값이 존재한다면
        else:
          # key값에 대한 value 들에 있어 방문하지 않은 곳이라면 출발 지점 노드의 길이 값보다 하나를 더해 덮어씌워준다.
          for next_city in graph[front]:
              if distance_list[next_city] == -1:
                  distance_list[next_city] = distance_list[front] + 1

                  #그리고 그 다음 출발 지점을 queue에 뒤에 붙여준다.
                  que.append(next_city)

    # 길이가 담긴 리스트를 반환한다.
    return distance_list


distance_result = bfs(graph, start_city)   ###  [-1,0,1,1,2]

result = []

# 이제 찾고자 하는 길이(2)에 대하여 같은 부분들만 idx 번호를 새로운 리스트 result에 append 해준다.
for i in range(city_num+1):
    if distance_result[i] == distance:
        result.append(i)

# append 된 것이 하나라도 있다면 result를 출력하고 없다면 -1을 출력한다.
if result:
    print(result)
else:
    print(-1)
