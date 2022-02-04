N, M = map(int, input().split())
nums = list(map(int, input().split()))
total = sum(nums)
max_num = max(nums)
min_nums = min(nums)

answer = 0


def BSearch_rice(N: int, M: int, nums: list[int]) -> int:
    global total
    global max_num
    global min_nums
    global answer

    temp = total - N * min(nums)

    if temp > M:
        start = min_nums + 1
        end = max_num
        answer = start

        while start < end:
            if total - N * answer < M:
                return answer + 1
            elif total - N * answer == M:
                return answer
            else:
                start += 1
                answer = start

    elif temp == M:
        answer = min_nums
        return answer

    else:
        start = 0
        end = min_nums - 1
        answer = start

        while start < end:
            if total - N * answer < M:
                return answer + 1

            elif total - N * answer == M:
                return answer
            else:
                start += 1
                answer = start

    return answer


print(BSearch_rice(N, M, nums))


######################################

