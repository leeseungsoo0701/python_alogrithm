"""
문제 : 중복 문자가 없는 가장 긴 부분 문자열의 길이를 리턴하라.
입력 : "abcabcbb", "bbbbbb"
출력 : 3 ,  1


abba

a: 0           start  0  answer 0
b: 1           start  0  answer 1
b: 2           start  2  answer 2
a :3           start  2



abcac
아이디어:
"""

def withoutRepeat(S:str)->int:
    dic = {}
    answer = 0
    start = 0


    for i,str in enumerate(S):
        if str in dic.keys() and start <= dic[str]:
            answer = max(answer, (i - start))
            start = dic[str] + 1

        dic[str] = i

    return max(answer, len(S[start:]))



S = "abbbbbabcded"
print(withoutRepeat(S))

#######################################
def withoutRepeat(S1: str) -> int:
    check = []
    count = 0
    length = 0
    for word in S1:
        if word not in check:
            check.append(word)
            count +=1
        else:
            length = max(count,length)
            count = 0
            check = []

    return length





S1 = "abcabcbb"
print(withoutRepeat(S1))
