from collections import deque


def solution(prices):
    answer = []
    queue = deque()

    for i, price in enumerate(prices):
        queue.append([price, i])

    while queue:
        time = 0
        temp = queue.popleft()

        for left_queue in queue:
            time += 1
            if left_queue[0] < temp[0]:
                break

        answer.append(time)

    return answer