"""
n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수 를 출력하라.
입력 [1,4,3,2]
출력 4
"""


def array_partition(nums):  #받을 변수를 적어줘야한다.(형태 상관 무)
    total = 0  #결과값을 나타낸 것이다.
    pair = []  #빈 배열로 기존 배열의 값들을 2개씩만 채워주기 위함이다.
    nums.sort()  #정렬을 하여 2개씩만 뽑아내고 그 중 앞의 수만 뽑아내면 되기에 정렬해 놓은 것이다.

    for i in nums:          #입력 받은 배열의 수를 빈 배열에 차곡차곡 넣는다
        pair.append(i)

        if len(pair)==2:    #pair 배열의 길이가 2가 되는 순간
            total +=pair[0]  #들어온 값 중 앞 부분을 total에 더해주고
            pair = []       #pair을 초기화 시켜준다
    return print(total)


nums = [1,4,3,2]
array_partition(nums)


###########################
def array_sum(nums):
    total = 0       #결과값을 나타내기 위한 변수
    nums.sort()     #정렬하여 index가 짝수인 것들만 더해주면 되기에 정렬하는 것이다.

    nums = nums[::2]  #기존 배열의 슬라이싱을 통하여 짝수 인덱스만 포함되도록 만들고
    total = sum(nums)  #리스트 안의 것들을 도와주기 위한 sum 함수를 사용하고 total에 넣어준다.

    print(total)        #total을 출력한다.


nums = [1,4,3,2]
array_sum(nums)
############################
