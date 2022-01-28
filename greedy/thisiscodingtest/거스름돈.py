"""
거스름돈을 입력 받고
최소한의 동전으로 반납하라

아이디어 :  아이디어로는 가장 적게 주려면 큰 값부터 하나씩 빼주면 된다 언제까지?
더이상 못 빼줄 때까지
== 몫과 나머지를 활용하면 된다.
"""

import sys


## 입력 받기
N = int(sys.stdin.readline())


## 큰 수부터 배열에 넣기
coins = [500,100,50,10]

## 최종 동전의 갯수 파악하기 위한 변수 생성
count = 0

## coins안에 있는 값을 활용하기 위한 for coin in coins
for coin in coins:

    ## divmod 라이브러리를 이용한 몫을 n, 나머지를 m에 저장
    n,m = divmod(N,coin)

    ## 전체 동전 갯수를 구하기 위함임로 count에 몫을 저장
    count += n

    ## 거스름돈을 준 나머지를 다시 계산하여야하기 때문에 거스름돈을 N으로 변환
    N = m

print(count)