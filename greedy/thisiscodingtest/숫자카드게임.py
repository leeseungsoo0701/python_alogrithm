"""
아이디어 : 이중 배열로 input을 받은 뒤 각 인덱스에 해당하는 것을 입력 받을때!
sort 시켜줘서 가장 최솟값을 result 배열에 넣는다.
result 배열에는 각 행의 최솟값들이 모여있을 것이다. 여기서는 max를 써도 좋고 sort한 후 [-1]에 해당하는 값을 도출하여도 좋다.
"""

# 두 가지 int 형을 스페이스 기준으로 split하여 입력 받기 위한 코드
m,n = map(int,input().split())


#각 행에 대하여 입력 받고 넣어줄 리스트 생성
nums = []

# 최솟값을 넣어줄 리스트 생성
result =[]

# 각 행의 길이에 대하여 (열의 길이는 필요 없다) 입력을 받자
for i in range(m):

    # 여기서도 스페이스바를 기준으로 각 숫자들을 nums에 append한다.
    nums.append(input().split())

    #for문 안에서 각 인덱스에 해당하는 값들을 sort해준다(각 행의 최솟값을 알기 위하여) 여기서 인덱스는 결국 각 행에 해당한다.
    nums[i].sort()

    #result 배열에 각 행의 최솟값들을 append 해준다.
    result.append(nums[i][0])

#result 배열의 가장 최댓값을 answer로 리턴하고 그 값을 출력하면 끝난다.
answer = max(result)
print(answer)





