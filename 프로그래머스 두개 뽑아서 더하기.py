def solution(numbers):
    answer = []
    numbers.sort()

    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            total = numbers[i] + numbers[j]
            if total not in answer:
                answer.append(numbers[i] + numbers[j])

    answer.sort()
    return answer