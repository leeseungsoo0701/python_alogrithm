# 입력 받는 사람의 수
N = int(input())

# 인원의 공포도
X = input().split()

#공포도가 낮은 순으로 정렬
X.sort()

#인원에 대한 결과 변수 설정
result = 0

#공포도 비교를 위한 변수 설정
count = 0


for idx, val in enumerate(X):
    # 공포도와의 비교를 위한 count의 증가
    count += 1

    # 늘어난 count가 idx보다 크거나 같아지면 하나의 그룹이 생성되므로 result를 1 추가하고 count를 초기화 시켜준다.
    if idx <= count:
        result += 1
        count = 0

print(result)
