"""
문제 : 배열을 입력 받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하라
입력: [1,2,3,4]
출력: [24,12,8,6]

아이디어:
"""

def arrayExecptSelf(inputs:list[int])->list[int]:
    mul = []
    total = []
    for idx in range(len(inputs)):
        sum = 1
        # print(type(inputs[idx]))
        # print(idx)
        # print(inputs[idx])
        mul.append(inputs[idx])
        inputs.remove(inputs[idx])
        # print(inputs)

        for j in range(len(inputs)):
            sum *= inputs[j]
            # print(sum)

        total.append(sum)

        inputs.insert(idx,mul[idx])

    return total

inputs = [1,2,3,4]
print(arrayExecptSelf(inputs))



##################################
