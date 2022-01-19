"""
문제: 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라 대소문자 구분을 하지 않으며, 구두점 또한 무시한다.

입력: paragraph = "Bob hit a ball, the hit BaALL flew far after it was hit."
banned = ["hit"]

출: "ball"

아이디어: 1.우선 맨 처음에는 입력 받은 문자열을 소문자로 치환하여 split 후 새로운 리스트 split_p에 넣어준다
        2. 이 과정에서 각 리스트에 존재하는 것 중에 banned에 해당하는 문자열이 존재 시 pass를 하고 banned에 걸리지 않는데
        3. 리스트 요소 중 구두점이 있을 시, 구두점을 제거하고 new_lists에 넣어준다.
        4. new_list를 counter를 활용하여 가장 많이 나온 단어를 출력한다.
"""

from collections import Counter
def commonWord(paragraph : str, banned: list[str]) -> str:
    lower_p = paragraph.lower()
    new_lists = []
    split_p = lower_p.split()
    print(split_p)

    print(banned[0])
    for word in split_p:
        if  word == banned[0]:
            pass
        elif '.' in word or ',' in word:
            word = word[:-1]
            new_lists.append(word)
        else:
            new_lists.append(word)

    count_p = Counter(new_lists)
    print(count_p)
    print(count_p.most_common(1)[0][0])

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
commonWord(paragraph,banned)