
def solution(d, budget):
    d.sort()
    cnt = 0

    for i in d :
        budget -= i
        if budget < 0 :
               break
        cnt += 1
    answer = cnt
    return answer



###############################

def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)