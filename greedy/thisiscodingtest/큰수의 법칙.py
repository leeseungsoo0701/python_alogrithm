"""
M과 K가 주어지는데 M은 총 더하는 횟수
K는 연속해서 더해질 수 있는 갯수이다.
즉 이 문제에서는 가장 큰 값을 k번 더하고 그 다음의 가장 큰 값을 하나 더한 뒤 나머지에 대해서도 가장 큰 값을 k번 더하면 된다
총 횟수는 M안에서


아이디어 : 리스트를 sort한 뒤 가장 큰 값과 두번째로 큰 값을 미리 지정한다.
여기서 케이스 1,2 로 갈린다
만약 M == K라면 그냥 가장 큰 값에 K를 곱하면 끝나는 것이고
그것이 아니라면 K가 M보다 1이라도 작기에 무조건 두번째로 큰 값이 한번은 껴 있어야한다.
그 얘기는 즉슨 한 번 더할 때 max_num*K + second_num을 하나의 덩어리로 빼준다면 위 로직을 수행할 수 있다.
그 후에 나머지들을에 max를 곱해주면 된다!
"""
import sys
# 입력 받기
N,M,K = map(int,sys.stdin.readline().split())

#배열 입력 받기
nums = list(map(int,sys.stdin.readline().split()))

# 결과값을 위한 result = 0 생성
result = 0

#최대값을 찾기 위한 nums sort
nums.sort()

#최댓값 찾기
max_num = nums[-1]

#두번째로 큰 값 찾기
second_num = nums[-2]

## 전체 바퀴를 돌릴 횟수에 대한 파악 몫 구하기
cycle = M // (K+1)


## 처음부터 아예 M과 K가 똑같더라면 그냥 최댓값을 K번 곱해주면 된다.
if M == K:
    result = max_num * K

## 그게 아니라면 무조건 K+1 <= M을 만족하므로 위 for문이 성립될 수 있다.
else:
    # cycle이 몫이므로 무조건 M은 0보다 크다 저 계산을 하여도
    # 그러면 이제 K+1 즉 두번째로 큰 숫자까지 엮어서 한번에 계산해준다 마치 원래 같은 식구였던 것처럼
    for _ in range(cycle):
        result = result + max_num*K
        result = result + second_num*1
        M = M - (K+1)

    ## 딱 나누어떨어지면 어차피 M이 0이므로 result에 더해질 것이 없지만 남은 짤짤이가 있다면 무조건 max_num을 곱해줘야
    ## 최대값이 나오기 때문에 나머지 잔털어준다.
    result += max_num*M


## 결과값 프린트
print(result)

