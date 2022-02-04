"""
numbers = [2,8,11,15]
taget = 9

[1,2]

"""
numbers = list(map(int, input().split()))
numbers.sort()
print(numbers)

target = int(input())


def twoSum(numbers: list[int], taget: int) -> list[int]:
    left = 0
    right = len(numbers) - 1

    while left < right:
        if numbers[left] + numbers[right] < taget:
            left += 1
        elif numbers[left] + numbers[right] > taget:
            right -= 1
        else:
            return [left+1, right+1]

    return [-1]


print(twoSum(numbers, target))


################################################################


