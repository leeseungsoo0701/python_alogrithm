# 입력 받을 갯수
N = int(input())

# 입력 받을 수 int형으로 받기(map)
nums = list(map(int, input().split()))
# print(nums)

# 정렬 후 작은 수부터 더해주기
nums.sort()

# 자연수라는 가정하에 진행
total = 1

# 횟수는 입력 받은 갯수만큼 진행
for num in nums:
    # total의 수가 각 리스트의 값보다 작을 시 for문 종료
    if total < num:
        break

    # 아니라면 그냥 더해주기
    total += num

print(total)



