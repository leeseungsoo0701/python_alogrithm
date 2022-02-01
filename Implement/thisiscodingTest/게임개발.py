"""

"""
# 전체 받은 문자열 입력
num = list(input())

# 좌측 시작은 0
left = 0

# 우측 끝은 len(num) - 1  인덱스의 끝이므로 -1 해줘야한다.
right = len(num) - 1

# 좌측 총값
left_total = 0

# 우측 총값
right_total = 0

# 좌측 +, 우측 - 해가며 범위를 좁힌다.
while left <= right:
    left_total += int(num[left])
    right_total += int(num[right])

    left += 1
    right -= 1

# 값이 일치하면 프린트 LUCKY
if left_total == right_total:
    print("LUCKY")
else:
    print("READY")
