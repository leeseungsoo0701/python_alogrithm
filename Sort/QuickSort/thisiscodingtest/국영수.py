"""
12
Junkyu 50 60 100
SangKeun 80 60 50
Sunyoung 80 70 100
Soong 50 60 90
Haebin 50 60 100
Kangsoo 60 80 100
Donghyuk 80 60 100
Sei 70 70 70
Wonseob 70 70 90
Sanghyun 70 70 80
nsj 80 80 80
Taewhan 50 60 90
"""
# 갯수 입력 받기
N = int(input())

# 이중 배열을 포함하기 위 리스트 생성
p_list = []

# 각각의 값들 넣어주기
for _ in range(N):
    p_list.append(list(map(str,input().split())))

# idx:1(국어) idx:2(영어) idx:3(수학) idx:0(이름)
p_list.sort(key=lambda x:(-int(x[1]),int(x[2]),-int(x[3]),x[0]))

# 이름만 출력
for i in range(N):
    print(p_list[i][0])
