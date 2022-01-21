"""
아이디어 : 가장 윗 노드 빈걸로 생성
그 다음 노드는 1,2,3인데
이제 길이가 처음 입력받은 길이(3)까지가 백트랙킹하고
append해주면 된다.



"""
from collections import deque

def permutatuions(nums : list[str])->list[list[int]]:
    result = []
    nums = deque(nums)
    #base case
    if (len(nums) ==1):
        return [nums]

    for i in range(len(nums)):
        n = nums.popleft()

        perms = permutatuions(nums)  ############### perms???????

        for perm in perms:
            perm.append(n)

        result.extend(perms)
        nums.append(n)

    return result






nums = [1,2,3]
print(permutatuions(nums))