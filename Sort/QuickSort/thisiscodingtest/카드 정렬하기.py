from collections import deque

# 입력 받을 갯수
N = int(input())

#저장할 리스트 생성
cards = []

for _ in range(N):
    card = int(input())
    cards.append(card)

#작은 순대로 정렬
cards.sort()

#popleft를 활용하기 위한 deque
cards = deque(cards)

total = 0

while cards:
    # 길이가 2 이상이여야지 2개를 pop할 수 있기에 적어놓고
    if len(cards) > 1:
        temp_1 = cards.popleft()
        temp_2 = cards.popleft()

        total = total + temp_1 + temp_2

        #total을 다시 왼쪽에 넣어주면서 계속 더해준다.
        cards.appendleft(total)

    # 길이가 1이하가 된다면 이미 수행이 다 돌아간 것이므로 break한다.
    else:
        break

print(total)

