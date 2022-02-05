"""
4 11
802
743
457
539


"""

import sys

K, N = map(int, input().split())

nums_list = [int(input()) for i in range(K)]
nums_list.sort()


def len_line(N: int, nums_list: list[int]) -> int:
    left = 1
    right = max(nums_list)

    while left <= right:
        mid = (left + right) // 2

        count = 0
        for num in nums_list:
            count += num // mid

        if count >= N:
            left = mid + 1
        else:
            right = mid - 1

    return right


print(len_line(N,nums_list))