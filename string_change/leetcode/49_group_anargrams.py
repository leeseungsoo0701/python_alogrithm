"""
문자열 배열을 받아 애너그램 단위로 그룹핑하라

입력 : ["eat", "tea", "tan", "ate", "nat", "bat"]
출력: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

아이디어: 1.딕셔너리는 value로 리스트를 가질 수 있다.
        2. 각 문자를 하나하니씩 정렬하면 같은 문자가 들어있는 정보들은 모두 하나의 key로 치환된다.
        3. 이제 키를 해당으로 dic에 하나하나 데이터를 넣어줘야하는데 맨 처음 key값이 없을 시,
        4. 하나 만들어주고 이미 존재 시 , append를 하면 리스트로 저장이 된다.
        5. dic의 value를 보여주려면 dic.values()를 활용하면 된다.
"""



def groupAnagrams(strs):
    dic = {}     #Key, Value를 설정하기 위해서 디렉토리를 생성

    for word in strs: #strs 리스트에 존재하는 word를
        key = "".join(sorted(word))  #하나하나 알파벳으로 정렬해준다 acb -> abc

        if key not in dic.keys():   #맨처음의 경우와 중복되는 키 값이 없는 경우에는 딕셔너리의 value 값으로 리스트를 설정해줘야하기 때문에 리스트를 생성힌다.
            dic[key] = [word]       #default dic에 대해서 확인하면 이 과정이 없어도 된다.

        else:
            dic[key].append(word)    # 아닌 경우에는 이미 존재하는 리스트에 append로 단어를 추가해준다.

    print(dic)

    # 마지막으로 딕셔너리의 값들을 다 뽑아내면 이미 리스트 형태로 value가 들어있지만 출력은 각 값이 같은 것들의 리스트를 또 리스트로 묶어주었기에 list로 감싼다.
    return list(dic.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))

