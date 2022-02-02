# 입력 받을 갯수
N = int(input())

#임의의 stages 수
stages = list(map(int,(input().split())))

#돌려야할 갯수 미리 지정
len_stages = len(stages)

#작은 순으로 정렬
stages.sort()

#결과를 나타낼 리스트 생성
result = []

# 스테이지는 1부터이므로 1~N 까지
for i in range(1,N+1):

    #각 i에 대한 값을 가진다
    count = stages.count(i)

    # 만약 stages가 0이라면 fail을 0 처리해준다(len_stages -= count를 진행하면서 len_stages가 0이 될 때는 결국 아무도 도달하지 못하는 stage의 경우 실패율을 0처리
    # 해줘야하기 때문에)
    if len_stages == 0:
        fail = 0

    # 아닌 경우네는 그냥 나눠주면 된다.
    else:
        fail = count / len_stages


    # 실패율이 동일한 경우 인덱스도 포함하여야하기 때문에 튜플 형태로 저장해준다.
    result.append((fail,i))

    # 분모가 달라져야하므로 counting 된 갯수만큼 빼주어 다시 지정해준다.
    len_stages = len_stages - count

# sort를 실패율, idx 번호 순으로 람다 함수를 이용하여 정렬한다. reverse를 하고 싶다면 앞에 -를 붙이면 된다.
result = sorted(result,key=lambda sorted_result:(-sorted_result[0],sorted_result[1]))

print(result)

# 결과에 대한 인덱스번호만 추출한다.
result = [j[1] for j in result]

# 프린트한다.
print(result)
