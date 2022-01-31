"""



"""
# 입력 받을 수의 집합
N = int(input())

# 결과값 세팅
result = 0

#분 초에 대해서만 결과값 도출
for i in range(60):
    for j in range(60):
        if '3' in str(i) + str(j):
            result += 1

# 시간은 3, 13 , 23일 때는 뒤의 모든 분초가 성립하므로 3600씩 더해준다.
if 0 <= N < 3:
    result = result * (N + 1)
elif 3 <= N < 13:
    result = result * N + 3600*1
elif 13 <= N < 23:
    result = result * (N - 1) + 3600*2
else:
    result = result * (N - 2) + 3600*3

print(result)
