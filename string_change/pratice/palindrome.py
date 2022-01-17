###pop 방식

def isPalindrome(self, s: str) -> bool:
    strs = []


    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True






### reverse 방식

def isPalindrome(self, s: str) -> bool:
    valid_list = [i.lower() for i in s if i.isalnum()]
    rev_valid_list = valid_list[::-1]
    return valid_list == rev_valid_list  ###같으면 True
