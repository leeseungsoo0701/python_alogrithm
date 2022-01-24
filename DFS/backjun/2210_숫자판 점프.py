import sys

sys.setrecursionlimit(10 ** 9)


k = [list(map(str, input().split())) for _ in range(5)]

print(k)

result = []
answer = ''
count = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs_numberPad(x, y):
    global answer
    global count

    if count == 6:
        count = 0
        result.append(answer)
        answer = ''
        return

    else:
        if x < 0 or x >= 5 or y < 0 or y >= 5:
            return

        else:
            count += 1
            answer += str(k[x][y])
            for j in range(4):
                dfs_numberPad(x + dx[j], y + dy[j])


for q in range(5):
    for w in range(5):
        dfs_numberPad(q, w)

print(result)


######################################

def dfs(x,y,number):
  if len(number)==6:
    if number not in result:
      result.append(number)
    return

  dx=[1,-1,0,0]
  dy=[0,0,1,-1]
  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]
    if nx<0 or nx>=5 or ny<0 or ny>=5:
      continue
    else:
      dfs(nx,ny,number+board[nx][ny])

board=[]
for i in range(5):
  board.append(list(map(str, input().split())))

result=[]
for i in range(5):
  for j in range(5):
    dfs(i,j,board[i][j])
print(len(result))