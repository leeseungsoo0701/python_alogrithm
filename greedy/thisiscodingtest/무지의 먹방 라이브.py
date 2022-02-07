K = int(input())
food_times = list(map(int, input().split()))

array = []


def mukbang(food_times: list[int], K: int) -> int:
    for idx, val in enumerate(food_times):
        array.append([val, idx])

    total = sum(food_times)

    if total <= K:
        return -1

    count = 0
    len_food_times = len(food_times)
    min_food_times = min(food_times)
    cycle = K // len_food_times
    etc = K % len_food_times

    if cycle <= min_food_times:
        count += cycle * len_food_times
        K -= count
        for i in range(len_food_times):
            array[i][0] = array[i][0] - cycle

    else:
        etc += (cycle - min_food_times) * len_food_times
        cycle = min_food_times
        count += cycle * len_food_times
        K -= count
        for j in range(len_food_times):
            array[j][0] = array[j][0] - cycle

    for k in range(etc):
        if array[k][0] == 0:
            continue
        else:
            array.append(array[k][0] - 1)
            count += 1

    return array[count//len_food_times][1]


print(mukbang(food_times, K))



############################################################
K = int(input())
food_times = list(map(int, input().split()))

array = []


