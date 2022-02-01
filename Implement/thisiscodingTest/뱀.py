import copy

dic = {"R": [0, 1], "L": [0, -1], "U": [-1, 0], "D": [1, 0]}

N = int(input())

K = int(input())

baam = []

for _ in range(N):
    baam.append([0 for _ in range(N)])

# 방문한 곳 체크
visited = copy.deepcopy(baam)

# 변환 리스트
move = []

# 사과의 위치 입력 받기
for _ in range(K):
    a, b = map(int, input().split())
    baam[a - 1][b - 1] = 1

print(baam)
print(visited)

# 회전의 수
L = int(input())

# n 초 뒤의 방향 전환 입력 받기
for _ in range(L):
    move.append(list(map(str, input().split())))

time = 0

# def snake():
