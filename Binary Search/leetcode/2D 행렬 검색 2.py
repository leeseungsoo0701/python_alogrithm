"""
m*n 행렬에서 값을 찾아내는 효율적인 알고리즘 구현


5 5
5
1 4 7 11 15
2 5 8 12 19
3 6 9 16 22
10 13 14 17 24
18 21 23 26 30


"""
N, M = map(int, input().split())
target = int(input())

nums = []
for _ in range(N):
    nums.append(list(map(int, input().split())))

print(nums)


def twoD(nums: list[list[int]], target: int) -> bool:
    for i in range(len(nums)):
        if target < nums[i][0]:
            continue

        if target in nums[i]:
            return True

    return False


print(twoD(nums, target))

# def twoD(nums:list[list[int]],target: int)->bool:
#     for i in range(len(nums)):
