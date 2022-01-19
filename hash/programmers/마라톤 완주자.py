def solution(participant, completion):
    answer = ''
    dic = {}

    for idx, val in enumerate(participant):
        if  val in dic.keys():
            dic[val] += 1
        else:
            dic[val] = 1

    for idx, val in enumerate(completion):
        if val in dic.keys():
            dic[val] -= 1
        else:
            pass

    for idx, val in enumerate(dic):
        if dic[val] == 1:
            answer = val


    return answer


participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
print(solution(participant,completion))