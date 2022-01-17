######### 괄호가 정확하게 들어가있는지 확인해라
######### 앞에꺼 있으면 push하고 뒷부분 나오면 key value로 앞에 값 확인하여 비교한다.



from stack_queue.structures import Stack
def is_valid(s):
    pair = {
        '}' : '{',
        ')' : '(',
        ']' : '['
    }
    opener = "({["  ### 앞부분

    stack = Stack()

    for char in s:
        if char in opener:
            stack.push(char)
        else:
            if stack.is_empty():
                return False
            if pair[char] != stack.pop():
                return False

    return stack.is_empty()   #### 프로세스가 다 끝나고




print(is_valid("{}()[]"))
assert is_valid("{[]}")


assert is_valid("{}]")
