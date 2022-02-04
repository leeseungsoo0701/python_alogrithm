import itertools

# 입력 받을 수 입력 받기
N = int(input())

# 숫자들 입력받기(list 형태로)
nums = list(map(int, input().split()))

# 연산자 갯수 입력 받기
plus, minus, mult, div = map(int, input().split())

# 연산자들 넣어주기
result = ['+'] * plus + ['-'] * minus + ['*'] * mult + ['/'] * div
print(result)

# 최댓값 최솟값 비교를 위한 값 미리 넣어두기
max_n = -9999999999
min_n = 9999999999

# permutations라는 순열 라이브러리를 활용하여 모든 경우의 수를 판단한 후, set을 시킨다
# ? 왜 set을 시키냐하면 순열이래서 +*+이면 이게 2번 나올 수 있기 떄문에 중복을 제거해준다.(세트에 대한 중복 제거)
cal_per = set(itertools.permutations(result, len(result)))
print(cal_per)

#각 값에 대해서 계속하여 위 함수에 넣어주면 되는 것이고 함수의 파라미터로는 각각의 값과 연산자 하나이다.
def calculator(x, y, c):
    if c == '+':
        return x + y
    elif c == '-':
        return x - y
    elif c == '*':
        return x * y
    else:
        if x < 0:
            return -((-x) // y)
        return x // y

#### 넣어준 연산자 조합의 집합에 대해서
for i in cal_per:
    result = 0
    # len(i) = plus + minus + mul + div이다.
    for j in range(len(i)):
        # 맨 처음에는 nums의 첫번째 수와 두번째 수에 대해서 연산자의 첫번째 것과 계산해야한다.
        if j == 0:
            result = calculator(nums[j], nums[j + 1], i[j])

        # 그 다음부터는 계산된 결과값과 그 다음수와의 연산을 진행하면 된다.
        else:
            result = calculator(result, nums[j + 1], i[j])

    # 그 결과가 현재 최댓값보다 작다면 결과가 최솟값이 되고
    if result < min_n:
        min_n = result

    #최솟값보다 크다면 그 결과가 최댓값이 된다.
    if result > max_n:
        max_n = result

print(max_n)
print(min_n)

# answer = []
#
#
#
# nums_queue = deque(nums)
#
#
# def BFS(nums: list[int], result: list[int]) -> list[int]:
#     while nums_queue:
#         num = nums_queue.popleft()
#         if len(nums_queue) >= 1:
#             for i in range(len(result)):
#                 if result[i][1] == 0:
#                     continue
#                 else:
#                     if result[i][0] == '+':
#                         for _ in range(result[i][1]):
#                             nums_queue.appendleft(num + nums_queue.popleft())
#                     if result[i][0] == '-':
#                         for _ in range(result[i][1]):
#                             nums_queue.appendleft(num - nums_queue.popleft())
#                     if result[i][0] == '*':
#                         for _ in range(result[i][1]):
#                             nums_queue.appendleft(num * nums_queue.popleft())
#                     if result[i][0] == '/':
#                         for _ in range(result[i][1]):
#                             if num > 0:
#                                 nums_queue.appendleft(num // nums_queue.popleft())
#                             else:
#                                 nums_queue.appendleft(-(abs(num) // nums_queue.popleft()))
#
#         else:
#             return answer.append(nums_queue[0])
#
#
# KKK = BFS(nums,result)
#
# print(max(KKK))
# print(min(KKK))
