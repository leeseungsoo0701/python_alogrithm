"""
문제: 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다.
예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만,
aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

입력 : 3
happy
new
year

출력 :
3

아이디어: 1.

"""
## 입력 받을 문자열 받기
num = int(input())

## 전체에서 안되는 문자열의 갯수를 빼기 위한 전체 문자 갯수 대입
result = num

for i in range(num):

    # 문자 대입
    word = str(input())

    ## len(word)-1인 이유는 j+1과 비교해야하기에 index에러가 나올 수 있고 맨 마지막은 검사할 필요가 없기 때문에 이렇게 적어놓는다
    for j in range(len(word)-1):
        if word[j] == word[j+1]:
            pass

        ## 뒤에서 앞의 문자를 확인하는 것이 아닌 앞에서 뒤에 남은 것들 중 하나라도 있으면 이제 결과에서 하나를 뺀다. 그리고 그 즉시 break해서 빠져나온다.
        elif word[j] in word[j+1:]:
            result -=1
            break


print(result)


