"""
A = [1,2,5,4,3]
B = [5,5,6,6,5]

N =5
K =3
"""
from collections import deque

# 두개의 int 입력 받기
N, K = map(int, input().split())

# int형을 여러개 입력 받고 그걸 list형태로 저장
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A는 작은 순으로 정렬 , B는 큰 수대로 정렬
A.sort()
B.sort(reverse=True)

# pop을 활용하기 위한 deque 설정
A = deque(A)
B = deque(B)

# K번 횟수를 지정하고 A의 가장 작은 수가 B의 가장 큰 수보다 크다면 break한다.
for i in range(K):
    temp = B.popleft()
    temp2 = A.popleft()

    if temp2 >= temp:
        A.appendleft(temp2)
        break

    # B의 원소가 더 크다면 어차피 A는 popleft로 날라갔고 B의 값을 A 뒤에 넣어주면 된다.(K<=N 이기에 뒤에 붙이면 더이상 비교 대상에 들어가지 않는다.)
    else:
        A.append(temp)

print(sum(A))
