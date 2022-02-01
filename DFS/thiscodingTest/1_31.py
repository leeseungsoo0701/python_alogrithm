"""
힙이 같은 부분 집합

"""
#6
#1 3 5 6 7 10

N = int(input())
# M = [i for i in range(1, N + 1)]
# # print(M)

nums = list(map(int, input().split()))
total = sum(nums)

res = "NO"

def DFS(level: int, sub_sum: int, idx: int):
    global res

    if res == "YES":
        return

    if level == N:
        return

    if total - sub_sum == sub_sum:
        res = "YES"
        return

    for i in range(idx, N):
        return DFS(level + 1, sub_sum + nums[i], i + 1)


if res == "YES":
    print("YES")
else:
    print("NO")
