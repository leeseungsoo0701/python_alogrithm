from collections import deque

def solution(food_times, k):
    food_times = deque([[value, idx] for idx, value in enumerate(food_times)])
    for _ in range(k):
        food_times[0][0] -= 1
        if food_times[0][0]:
            food_times.rotate(-1)
        else:
            food_times.popleft()
            if not food_times:
                return -1
    return food_times[0][1] + 1