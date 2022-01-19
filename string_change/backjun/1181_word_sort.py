"""
문제 :알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

길이가 짧은 것부터
길이가 같으면 사전 순으로

입력 :13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours

출력 :
13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours

"""

import sys


#### 적을 단어 갯수 입력
words_num = int(input())

### 최종 결과 리스트 생성
words_list = []

for i in range(words_num):

    ## for문 당 str을 input 받는다
    word = str(input())

    ## 길이가 짧은 순이므로 같이 입력 받는다
    word_len = len(word)

    ## 그 다음 결과리스트에 글자와 글자 길이를 넣어놓는다.
    words_list.append((word, word_len))

## 중복 제거를 위한 set해주고 다시 list화 시킨다.
words_list = list(set(words_list))

# print(type(words_list))


## lambda를 이용하여 word에 대하여 word의 길이 순 그 다음은 word로 정렬하라는 임의 함수 lambda를 사용한다.
words_list.sort(key= lambda word: (word[1],word[0]))

for word in words_list:
    print(word[0])