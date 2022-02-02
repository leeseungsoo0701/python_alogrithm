# 입력 받은 집의 갯수
N = int(input())

#안테나의 위치 입력
antenna = list(map(int, input().split()))
# 결과를 담을 리스트 생성
result = []

#최솟값을 찾기 위해서는 가장 초기값과 위치의 최대까지 돌아야한다.
for home in range(1, antenna[-1] + 1):

    # 각 집에서의 위치와의 길이를 측정하기 위한 리스트 생성 for문 돌때마다 초기화 시켜준다.
    min_size = []

    # 집의 위치를 빼주고 그걸 min_size에 넣어준다(abs 형태로)
    for i in range(len(antenna)):
        min_size.append(abs(home - antenna[i]))

    #튜플 형태로 인덱스와 각 위치에서의 길이를 result 리스트에 넣어준다.
    result.append((home,sum(min_size)))

#람다 함수를 이용하여 길이가 작은 순으로 정렬한다.
result = sorted(result, key=lambda minimum:minimum[1])

#인덱스를 출력해야하므로 가장 처음의 0을 출력한다.
print(result[0][0])





