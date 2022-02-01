def merge(intervals: list[list[int]]) -> list[list[int]]:
    result = []
    print(sorted(intervals))

    for interval in sorted(intervals):
        # print(interval)
        # print(type(interval))
        if result and interval[0] <= result[-1][1]:
            result[-1][1] = max(result[-1][1], interval[1])

        else:
            # print(type(interval))
            result.append(interval)

    return result


print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
