######### 주식을 사고 팔기 가장 좋은 시점
######### 입력: [7,1,5,3,6,4]
######### 출력: 5
def sellStock(inputs: list[int])->int:
    results = []
    for i in range(len(inputs)):
        results.append(max(inputs[i:]) - inputs[i])

    result = max(results)





    return result

inputs = [7,1,5,3,6,4]
print(sellStock(inputs))


#########################