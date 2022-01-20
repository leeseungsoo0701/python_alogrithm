
"""
나코더 기장 재민이는 동아리 회식을 준비하기 위해서 장부를 관리하는 중이다.

재현이는 재민이를 도와서 돈을 관리하는 중인데, 애석하게도 항상 정신없는 재현이는 돈을 실수로 잘못 부르는 사고를 치기 일쑤였다.

재현이는 잘못된 수를 부를 때마다 0을 외쳐서, 가장 최근에 재민이가 쓴 수를 지우게 시킨다.

재민이는 이렇게 모든 수를 받아 적은 후 그 수의 합을 알고 싶어 한다. 재민이를 도와주자!


첫 번째 줄에 정수 K가 주어진다. (1 ≤ K ≤ 100,000)

이후 K개의 줄에 정수가 1개씩 주어진다. 정수는 0에서 1,000,000 사이의 값을 가지며, 정수가 "0" 일 경우에는 가장 최근에 쓴 수를 지우고, 아닐 경우 해당 수를 쓴다.

정수가 "0"일 경우에 지울 수 있는 수가 있음을 보장할 수 있다.


입력 :
4
3
0
4
0

출력:
0

아이디어 : 0이 들어오면 pop해주고 아니면 append 해준 뒤 total을 sum(queue)를 통해 합계를 내준다.
"""



from collections import deque

num = int(input())
queue = deque()
total = 0
for i in range(num):
    answer = int(input())


    if answer == 0:
        queue.pop()
    else:
        queue.append(answer)


total = sum(queue)
print(total)

for i in range(num):
    answer = int(input())


    if answer == 0:
        queue.pop()
    else:
        queue.append(answer)


total = sum(queue)
print(total)
