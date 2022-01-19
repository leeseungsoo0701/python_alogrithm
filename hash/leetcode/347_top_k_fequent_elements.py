"""
상위 K번 이상 등장하는 요소를 추출하라.

입력 : nums = [1,1,1,2,2,3] k=2
출력 : [1,2]

아이디어: 위 리스트의 value에 대한 값을 counter를 통해 딕셔너리 형태로 만들고 그 중
딕셔너리의 value에서 k보다 큰 값에 대한 key 값을 list에 넣어 출력
"""
### 내장 함수 Counter를 활용한 찾기
from collections import Counter
def topK(nums : list[int], k:int)->list[int]:

    #결과를 담기 위한 리스트
    answer = []

    # counter를 활용한 딕셔너리 생성
    count_answer = Counter(nums)

    ## set을 한번 해줘서 중복값 제거
    set_nums = list(set(nums))


    # 하나하나 비교했을 때, 딕셔너리의 키 값에 무조건 있고 그 갯수를 k와 비교하면
    # answer에 apped 해주고 return하면 끝!
    for num in set_nums:
        if count_answer[num] >= k:
            answer.append(num)


    return answer


nums = [1,1,1,2,2,3,3,3,3]
k = 5
print(topK(nums,k))

