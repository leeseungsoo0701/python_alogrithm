######### 덧셈하여 타켓을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.
######### 입력 : nums = [2,7,11,15], target = 9
######### 출력 : [0,1]

def twoSum(nums: list[int], target: int)->list[str]:
    print(nums)
    print(type(target))
    nums.sort()

    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                print([i,j])



nums = [2,7,11,15]
target = 9
twoSum(nums,target)

##################


def twoSumTwoPoint(nums: list[int], target: int)->list[str]:
    print(nums)
    print(type(target))
    nums.sort()
    left, right = 0, len(nums)-1

    while left < right:
        if nums[left] + nums[right] < target:
            left +=1
        elif nums[left] + nums[right] > target:
            right -=1
        else:
            return [left,right]



nums = [2,7,11,15]
target = 9
print(twoSumTwoPoint(nums,target))