"""
주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.
ex) "abba" -> True
    "bbac" -> False
"""

###pop 방식
def isPalindrome(self, s: str) -> bool:
    strs = []

    #입력 받은 배열에 대하여 안의 원소들에 있어서 .isalnum()을 통하여 글자와 숫자만 새로운 배열 strs에 append하는데
    for char in s:
        if char.isalnum():
            strs.append(char.lower())   ### 소문자로 치환해서 append 해주는 것이다(문제의 조건)

    while len(strs) > 1:                ### strs 배열을 다 둘러봤을 때 맨 앞과 맨 뒤를 확인하기 위해서 pop을 사용하였고 위 과정이 중간에 걸린다면 false를 도출하도록 설계
        if strs.pop(0) != strs.pop():
            return False

    return True                         ### while 안의 if문에서 걸리지 않을 시, 팰린드롬이기에 return을 True로 하였다.






### reverse 방식
def isPalindrome(self, s: str) -> bool:
    valid_list = [i.lower() for i in s if i.isalnum()]              ##valid_list에 for문 사용 그런데 i의 lower를 넣는 것이고 if문을 사용하여 i가 isalnum일때만 작동하여 위 리스트에 들어간다
    rev_valid_list = valid_list[::-1]                               ## 새로운 배열 rev_valid_list를 만들어 valid_list의 뒤에서부터 넣어준다
    return valid_list == rev_valid_list  ###같으면 True, 틀리면 False를 반환하여 팰린드롬임을 확인할 수 있다.
