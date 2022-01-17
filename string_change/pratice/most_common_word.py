# 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라 대소문자 구분을 하지 않으며, 구두점 또한 무시한다.
# >
# > 입: paragraph = "Bob hit a ball, the hit BaALL flew far after it was hit."
#   banned = ["hit"]
# >
# > 출: "ball"

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