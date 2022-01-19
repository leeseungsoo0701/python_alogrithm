"""
문자열을 뒤집는 함수를 작성하라. 입력값은 문자 배열며 리턴없이 리스트 내부를 직접 조작하라

ex) 입력 ['h','e','l','l','o']
출력 ['o','l','l','e','h']

아이디어: 아이디어로는 입력 받은 배열을 새로운 배열에 하나하나씩 넣어주는 방법이 있었고
같은 배열에서 사용하려면 맨 뒤에 위치하는 인덱스와 맨 앞을 나타내는 인덱스를 바꿔주고 서로 앞으로 한칸 뒤로 한칸씩 이동하며 바꿔주는 투 포인터 방식을 생각하였다.
"""




def reverse_string(lists):

    """시작은 0이고 끝은 len(lists)-start-1이다.
    그 이유는 시작하고자하는 곳이 0 이기에 end = len(lists)-1이지 중간부터 바꾸고 싶다면
    start에 변수가 들어가고 end도 그에 맞게 해야하기 때문에"""

    start = 0
    end = len(lists)-start-1

    # 각자 인덱스에 해당하는 것들을 자료를 바꿔준다.
    while start < end:
        lists[start], lists[end] = lists[end], lists[start]
        start +=1
        end -=1

    print(lists)


s = list(input()) ######### 입력받은 문자열을 리스트 형태로 만들어주는 것
print(type(s))
print(s)
reverse_string(s)




############ 파이썬 내장 함수 사용하기(reverse)
def reverse_string_bypython(lists):

    # 리스트를 뒤집어준다.(import할 것도 없다)
    lists.reverse()
    print(lists)

h= list(input())
print(h)
reverse_string_bypython(h)