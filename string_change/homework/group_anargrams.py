##########################################################딕셔너리의 value를 리스트로 받을 수 있음을 알 수 있는 문제
def grouAnagrams(strs):
    dic = {}     #Key, Value를 설정하기 위해서 디렉토리를 생성

    for word in strs: #strs 리스트에 존재하는 word를
        key = "".join(sorted(word))  #하나하나 알파벳으로 정렬해준다 acb -> abc

        if key not in dic.keys():   #맨처음의 경우와 중복되는 키 값이 없는 경우에는 딕셔너리의 value 값으로 리스트를 설정해줘야하기 때문에 리스트를 생성하낟.
            dic[key] = [word]

        else:
            dic[key].append(word)    # 아닌 경우에는 이미 존재하는 리스트에 append로 단어를 추가해준다.

    print(dic)
    return list(dic.values())   # 마지막으로 딕셔너리의 값들을 다 뽑아내면 이미 리스트 형태로 value가 들어있지만 출력은 각 값이 같은 것들의 리스트를 또 리스트로 묶어주었기에 list로 감싼다.

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
#############################################################
