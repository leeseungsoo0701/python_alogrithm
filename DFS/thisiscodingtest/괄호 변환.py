from collections import deque
p = input()

queue = deque()

answer = True
def bracket(p:list[str])->str:
    global answer
    left = 0
    right = 0
    result = []
    u = []
    v = []

    for i in range(len(p)):
        if p[i] == '(':
            left +=1
            result.append('(')
        else:
            right +=1
            if len(result) == 0:
                answer = False
            else:
                result.pop()

        if left == right and answer:
            u = result[:i+1]
            v = result[i+1:]
            left = 0
            right = 0







print(bracket(p))