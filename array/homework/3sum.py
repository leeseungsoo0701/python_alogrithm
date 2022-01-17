######## 배열의 입력 받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라.
############# 1월 15일
############ 입력 : nums = [-1, 0, 1, 2, -1, -4]
############# -1 0 1 2 -1 -4
############ 출력 : [[-1,0,1],[-1,-1,2]]

class Solution:
    def threeSum(nums):
        answer = []   ### 정답을 담을 리스트
        nums.sort()   ### 음수 양수를 구분하기 위해서 정렬한다. (0은 양수 + 음수)

        # 가장 작은 값을 고정하고, 중간값과 큰 값을 투 포인터로 계산한다. (하나의 값을 고정하고 그 뒤부터 투 포인터로 좁혀가며 계산한다)
        # 고정값 index = start.
        for start in range(len(nums) - 2):

            # 한 번 고정값으로 사용했다면 건너뛴다.
            if start > 0 and nums[start] == nums[start - 1]:
                continue #하단의 코드를 실행하지 않고 넘어감 ,즉 같은 고정값이라면 패스한다.

            # 투 포인터로 간격을 줄여가며 합 계산
            left, right = start + 1, len(nums) - 1
            while left < right:
                sums = nums[start] + nums[left] + nums[right]
                # 0보다 작으면 left 위치를, 0보다 크면 right 위치를 이동시킨다.
                if sums < 0:
                    left += 1
                elif sums > 0:
                    right -= 1
                else:
                    answer.append([nums[start], nums[left], nums[right]])
                    # 중복연산 제거를 위해 left, right값 추가이동

                    # 같은 것이 두 번 들어갈 수도 있으므로 left나 right가
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        # for lists in answer:
        #     lists = sorted(lists)
        #
        # result = list(map(list,(set(map(tuple, answer)))))

        return print(answer)



    nums = [-1,0,1,2,-1,-4]
    threeSum(nums)