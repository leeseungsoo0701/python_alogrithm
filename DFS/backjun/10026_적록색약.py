N = int(input())


k = []
for i in range(0, N):
    k.append(list(map(str, (input()))))


count = 0
result = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]


def dfs_color(x,y,value):
    global count
    if x < 0 or x <= N or y < 0 or y <= N:
        return
    else:
        if k[x][y] == value:
            count+=1
        else:
            pass



    return (result[0], result[1])






dfs_color(0,0)

print(count)