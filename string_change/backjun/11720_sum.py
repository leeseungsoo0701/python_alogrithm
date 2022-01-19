"""
문제 : N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

입력 : 첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.
5
54321

출력 : 입력으로 주어진 숫자 N개의 합을 출력한다.
15


아이디어: 사용자에 입력 받은 문자열을 int로 바꿔서 전역 sum을 설정 후 그에 차곡차곡 더해주고 print하자.
"""

import sys

###몇 개를 입력 받을까에 대한 코드
n = int(sys.stdin.readline())

### 무엇을 입력하는지에 대한 코드로 list로 바로 받았다.
num = list(sys.stdin.readline())


sum = 0

### n만큼 sum에 num에 해당하는 자료들을 다 더해주면 끝
for i in range(n):
    sum += int(num[i])

print(sum)
