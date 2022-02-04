from collections import deque

#입력 받을 갯수 입력
N = int(input())

#비교를 위한 Deque 설정
nums = deque()

# 하나하나 입력 받아 deque에 넣어주기
for i in range(N):
    # 비교할 2개가 들어오기 전까지는 그냥 append
    nums.append(int(input()))

    # 비교할 2개가 들어오면 두개를 pop하여 비교하고 다시 append 해준다.
    if len(nums) >= 2:
        temp_top = nums.pop()
        temp_bottom = nums.pop()
        if temp_top > temp_bottom:
            nums.append(temp_top)
            nums.append(temp_bottom)
        else:
            nums.append(temp_bottom)
            nums.append(temp_top)

print(" ".join(list(nums)))



