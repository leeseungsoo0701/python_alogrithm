"""
힙이 같은 부분 집합

"""
#6
#1 3 5 6 7 10

N = 6 #int(input())

nums = [1,3,5,6,7,10] # list(map(int, input().split()))
total = sum(nums)

res = "NO"

def DFS(level: int, sub_sum: int, idx: int):
    global res

    if level == N or total/2 <= sub_sum:
        return

    if res == "YES":
        return res

    if sub_sum*2 == total:
        res = "YES"
        return

    for i in range(idx, N):
        return DFS(level + 1, sub_sum + nums[i], i + 1)


DFS(0,0,0)

if res == "YES":
    print("YES")
else:
    print("NO")
