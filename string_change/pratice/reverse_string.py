############### 문자열을 뒤집는 함수를 작성하라. 입력값은 문자 배열며 리턴없이 리스트 내부를 직접 조작하라

def reverse_string(lists):
    start = 0                               ####### 시작은 0이고 끝은 len(lists)-start-1이다.
    end = len(lists)-start-1
    while start < end:
        lists[start], lists[end] = lists[end], lists[start]
        start +=1
        end -=1

    print(lists)






s = list(input()) ######### 입력받은 문자열을 리스트 형태로 만들어주는 것
print(type(s))
print(s)
reverse_string(s)


#################################################### 파이썬 내장 함수 사용하기
def reverse_string_bypython(lists):
    lists.reverse()     ############ 리스트 안의 내용들을 뒤집어준다.
    print(lists)






h= list(input())
print(h)
reverse_string_bypython(h)