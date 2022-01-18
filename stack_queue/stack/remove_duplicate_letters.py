##################### 중복된 문자를 제외하고 사전식 순서로 나열하라
##################### 입력 "bcabc"
##################### 출력 "abc"
import collections


def removeDup(word: str)-> str:
    lists = list(word)
    result_A = sorted(list(set(lists)))
    print (result_A)

    letters = ""
    for s in result_A:
        letters += s

    print(letters)



word = ["bcabc", "cbacdcbc"]
removeDup(word[0])
removeDup(word[1])

##################################

def removeDup2(word: str)-> str:
    lists = list(word)
    stack = []

    for s in lists:
        if s not in stack:
            stack.append(s)

    result =  sorted(stack)
    print(result)



word = ["bcabc", "acdb"]
removeDup2(word[0])
removeDup2(word[1])


#######################
def removeDup3(words :str)-> str:
    list_word = list(words)
    print(list_word)
    stack = []
    seen = set()

    #
    # for word in list_word:
    #     while word
    #         if word in stack:

       # stack.append(word)




words = ["bcabc", "cbacdcbc"]
removeDup3(words[0])
removeDup3(words[1])