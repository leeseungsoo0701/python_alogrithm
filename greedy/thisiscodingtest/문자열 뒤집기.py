from collections import deque

#deque를 활용하여 값을 하나씩 popleft한 뒤 리스트가 아직 존재한다면 nums[0]과 비교하여 연속된 수인지 비교한다.
nums = deque(list(input()))

#zero는 0->1의 바뀌는 횟수이고 one은 1->0으로 바뀌는 횟수이다.
count_zero = 0
count_one = 0

#하나씩 pop하므로 한 바퀴를 돌리기 위한 nums이다.
while nums:
    temp = nums.popleft()

    #숫자는 0 아니면 1이므로 0일때와 else로 구분한다.
    if temp == '0':
        #리스트가 남아 있어야 비교가 가능하다.
        if nums:
            if nums[0] == temp:
                pass
            else:
                count_zero +=1
    else:
        if nums:
            if nums[0] == temp:
                pass
            else:
                count_one +=1


## 이 부분이 중요한데 무조건 count_zero와 count_one은 같거나 1 차이이다. 그럴 수 밖에 없는 구조이다.
## 그러면 이 상황에서 0011001 과 같이 0->1 2번 바뀌고 1->0은 1번만 바뀌지만 총 횟수는 2번을 해야하는 경우가 생긴다.
## 그렇기에 숫자가 똑같으면 그냥 프린트하고 만약 수가 다르다면 둘 중 작은 숫자 +1을 해주면 최소 값을 구할 수 있다.
if count_zero == count_one:
    print(count_zero)
else:
    print(min(count_zero,count_one)+1)



