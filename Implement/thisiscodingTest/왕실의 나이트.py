"""


"""
# 시작점에 대한 입력
Move = list(input())

#앞 부분이 열이고 뒷부분이 행이므로 세팅해준다. 또한 1부터 시작이므로 더하기 1을 해준다.
row = int(Move[1])
col = int(ord(Move[0]) - ord('a')) + 1

#움직일 수 있는 경우의 수들을 튜플로 리스트에 값으로 넣어둔다.
can_move = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, 2), (1, -2), (2, -1), (2, 1)]

#총 갯수 파악을 위한 변수 세팅
result = 0

# 리스트를 다 돌 때, 범위에 걸리면 result +=1을 해준다.
for move in can_move:

    #범위 안에 있으면 더해준다.
    if 1 <= col+move[0] <= 8 and 1 <= row+move[1] <= 8:
        result += 1

# 출력한다.
print(result)
