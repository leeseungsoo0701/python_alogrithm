"""주식을 사고 팔기 가장 좋은 시점
문제 : 한 번의 거래로 낼 수 있는 최대 이익을 산출하라
입력: [7,1,5,3,6,4]
출력: 5


아이디어: 리스트의 최댓값에서 현재 값을 뺀 것을 다른 리스트에 저장후
저장된 리스트에서의 max값을 찾아내면 된다.
"""


def sellStock(inputs: list[int])->int:
    results = []
    for i in range(len(inputs)):
        results.append(max(inputs[i:]) - inputs[i])

    result = max(results)





    return result

inputs = [7,1,5,3,6,4]
print(sellStock(inputs))


