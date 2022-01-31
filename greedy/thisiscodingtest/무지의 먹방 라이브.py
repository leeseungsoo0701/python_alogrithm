"""

"""
from collections import deque
food_times = list(map(int, input().split()))
K = int(input())

cycle, etc = divmod(K, len(food_times))
print(cycle, etc)

result = 0

# for i in range(len(food_times)):
#     food_times[i] = food_times[i] - cycle
#     if food_times[i] < 0:
#         result = -1
#         break
#
#
# # food_times = deque(food_times)
# # while food_times:
# #     temp = food_times.popleft()
# #     if temp == 0:
# #         continue
# #     if food_times:
# #         food_times[0] = food_times[0]-1
#
# for j in range(etc):
#     if food_times[j] == 0:
#         continue
#     else:
#         food_times[j] -= 1


print(result)
print(food_times)
