"""
괄호로 된 입력값이 올바른지 판단하라.

입력 : ()[]{}

출력 : true


아이디어:
1. dic를 만들어 각 괄호에 대한 key, value를 설정한다.
2. 앞부분의 문자열을 붙여서 만들고
3. stack에 openr문자열이 들어올 시, 추가하고 그 후에
4. 닫히는 괄호가 들어온다면 가장 위에 부분이랑 자리가 같아야하므로 pop했을 때의
5. 괄호와 키 value상 같아야한다.
6. 다르거나 stack이 없는데 닫히는게 들어온다면 return False를 한다.

"""


from stack_queue.leetcode.structures import Stack


def is_valid(s):

    # dic 만들어준다
    pair = {
        '}' : '{',
        ')' : '(',
        ']' : '['
    }
    opener = "({["  ### 앞부분

    stack = Stack()


    #전체 문자열을 하나씩 검색
    for char in s:

        #앞 부분에 있다면 stack에 넣기
        if char in opener:
            stack.push(char)

        #뒷 부분이라면
        else:

            #아무것도 없는 상태에서 뒷부분이 들어왔는지 확인
            if stack.is_empty():
                return False

            # 뒷부분이 들어왔다면 디렉토리에서 확인하고 맨 뒤에서 꺼내여 value와 pop이 일치하는지 확인
            # 일치하지 않다면 False 반환
            if pair[char] != stack.pop():
                return False

    return stack.is_empty()   #### 프로세스가 다 끝나고 다시 초기화




print(is_valid("{}()[]"))
assert is_valid("{[]}")


assert is_valid("{}]")
