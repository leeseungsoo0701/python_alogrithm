"""
7 2
1 1 2 2 2 2 3


7 4
1 1 2 2 2 2 3

"""
# counter 함수를 사용하기 위한 라이브러리
from collections import Counter

#각 값에 대한 key, value로 설정하기 위한 dic 생성
dic ={}
N, x = map(int,input().split())

nums = list(map(int,input().split()))

# Counter 함수를 사용한 Dic를 dic에 옮기고
dic = Counter(nums)


# 원하는 수 x가 dic 키에 있다면 그 value값(갯수)를 출력하고
if x in dic.keys():
    print(dic[x])

# 아니라면 print(-1)을 해준다.
else:
    print('-1')

