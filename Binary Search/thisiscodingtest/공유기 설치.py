# 집의 개수(N)와 공유기의 개수(C)를 입력 받기
n, c = map(int, input().split())

# 전체 집의 좌표 정보를 입력 받기
array = []
for i in range(n):
    array.append(int(input()))

array.sort()

# 가능한 최소 거리
start = 1
# 가능한 최대 거리
end = array[-1] - array[0]

result = 0

while start <= end:
    mid = (start + end) // 2 # mid는 가장 인접한 두 공유기 사이의 거리를 의미
    # 첫째 집에는 무조건 공유기를 설치한다고 가정
    pre = array[0]
    count = 1
    # 현재의 mid 값을 이용해 공유기를 설치하기
    # temp = 설치위치
    for temp in array[1:]: # 앞에서부터 차근차근 설치
        if temp >= pre + mid:
            count += 1
            pre = temp

    if count >= c: # C개 이상의 공유기를 설치할 수 있는 경우, 거리를 증가시키기
        start = mid + 1
        result = mid # 최적의 결과
    else: # C개 이상의 공유기를 설치할 수 없는 경우, 거리를 감소시키기
        end = mid - 1

print(result)