"""
5
-15 -6 1 3 7

7
-15 -4 3 8 9 13 15
"""
# 입력 값들 받기
N = int(input())
nums = list(map(int, input().split()))

# 좌 우 설정해주기
left = 0
right = N - 1


def BS_idx(N: int, nums: list[int]) -> int:
    # 전역변수 활용하기
    global left
    global right

    # res를 빈 문자열로 하여 만약에 고정점이 존재하면 위 문자열에 추가시켜주기
    res = ''

    # 좌측이 우측을 넘어가기 전까지 돌려준다.
    while left <= right:

        # 돌리면서 mid를 계속하여 갱신해준다.
        mid = (left + right) // 2

        # 실제 인덱스에 해당하는 값이 인덱스 값보다 작다면 오른쪽으로 이동해야하므로 left를 mid + 1로 해주고 right를 -1 해주면 된다.
        if nums[mid] < mid:
            left = mid + 1
            right -= 1

        # 계속 돌리다가 이제 정답이 나온다면 mid를 str으로 res에 넣어주고 break한다.
        elif nums[mid] == mid:
            res = str(mid)
            break
        # 아니라면 왼쪽으로 이동해야하므로 right를 mid -1로 left를 +1 해주면 된다.
        else:
            left += 1
            right = mid - 1

    # while문이 다 돌고 res가 있다면 print(res)로 str(mid)값을 보여주면 되고
    if res:
        print(res)
    # 없다면 print(-1)을 하면 된다.
    else:
        print('-1')


BS_idx(N, nums)
