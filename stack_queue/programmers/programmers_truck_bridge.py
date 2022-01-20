############# 우선 queue의 크기는 bridge_length를 넘으면 안된다.
############# 또한 queue에 들어있는 value 값들의 합이 weight보다 크면 안된다.



from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = deque()
    total = 0
    for i, v in enumerate(truck_weights):
        queue.append([v,i])

    while queue:
        temp = queue[0][0]
        total +=temp
        if total > weight:
            queue.popleft()
            total = 0
        else:
            queue.popleft()
            answer+=1

    return answer





bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
print(solution(bridge_length,weight,truck_weights))


################################


