"""
J는 보석이며, S는 갖고 있는 돌이다. S에는 보석이 몇개나 있을까?
대소문자는 구분한다.

아이디어: 긴 문자열에 해당하는 것들의 in을 사용하면 어차피 하나씩 나온다 그것 중 J에 있는지 확인만하고 있으면 count +=1을 해주면 된다.
"""


def numJS(J:str, S:str) -> int:
    count = 0
    for s in S:
        if s in J:
            count +=1
    return count



J = "aA"
S = "aAAbbbb"
print(numJS(J,S))