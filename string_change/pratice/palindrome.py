######## 1월 14일 연습 문제
#### Q1. 유효한 팰린드롬 (p.138)


### 반만 보면 된다 (홀수의 경우 가운데는 항상 같으므로 검사할 필요가 없다)
def isPalindrome(str):
    #moom
    #i:0,1 index 확인
    #j:3,2

    #예외처리
    str = str.lower()
    if not str.isalnum():
        return print(str + "은 palindorm이 아닙니다.")
    
    isPalin = True #default 값
    for i in range(1,len(str) // 2): # len(str) / 2 를 하면 홀수면 정확히 나눠지지 않으므로 float라 들어가지 않는다. 그 떄 사용하는 것은 // 이다.
        # j = len(str)-i-1       #index가 0부터 시작하기에 -1을 해줘야한다. 뒤에서부터 가는 것을 생각하면 i+j = len(s)-1
        # if str[i] != str[j]:
        #     isPalin = False
        #     break

        if str[i] != str[-i-1]: #0부터 실제로 생각해봐 j 없이도 뒤에꺼랑 비교하면 된다.
            isPalin = False
            break

    if isPalin == True:
        return print(str+"은 palindorm이 맞습니다")
    else:
        return print(str+ "은 palindorm이 아닙니다.")




if __name__ == "__main__": #pip8을 따른다?
    isPalindrome('mom')
    isPalindrome('kmmm')
