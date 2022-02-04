"""
합이 같은 부분 집합

"""
# 6
# {1 3 5 6 7 10}

#{1,3,5,7} {6,10}

# 입력 받을 갯수
N = 6  # int(input())

#부분 집합의 수 입력 받기
nums = [1, 3, 5, 6, 7, 10]  # list(map(int, input().split()))

# 우선 전체를 더해준다.
total = sum(nums)     #32

#
def DFS(level: int, sub_sum: int, idx: int):

    #끝까지 가거나 혹은 total//2보다 sub_sum이 커진다면 return false
    if level == N or total // 2 < sub_sum:
        return False

    # 만약에 더해지다가 같으면 return True
    if sub_sum * 2 == total:
        return True

    #DFS에 대한 return이 True, false를 반환하여 return 해준다.
    for i in range(idx, N):

        # DFS를 재귀로 돌려주면서 idx를 하나씩 뒤로 넘겨주면서 진행한다.
        if DFS(level + 1, sub_sum + nums[i], i + 1):
            return True

# return True이면 print("yes")
if DFS(0, 0, 0):
    print("YES")
else:
    print("NO")







#############################################
# cnt = int(input())
# numbers = list(map(map(int, input().split())))
# accum = sum(numbers)
# flag = False
#
# def dfs(L, res):
#     global flag
#
#     if flag == True:
#         return True
#
#     if L ==cnt or res > accum // 2:
#         if accum - res == res:
#             flag = True
#             return True
#         return False
#
#     return dfs(L+1, res+numbers[L])+dfs(L+1, res)
#
# result = dfs(0, 0)
# if result:
#     print("YES")
# else:
#     print("NO")
