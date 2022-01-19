"""
로그를 재정렬하라 기준은 다음과 같다.
1. 로그의 가장 앞 부분은 식별자이다.
2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
3. 식별자는 순서에 영향을 끼치진 않지만, 문자가 동일할 경우 식별자 순으로한다
4. 숫자 로그는 순서대로 한다.
입력 : logs = ['dig1 8 1 5 1","let1 art can","dig2 3 6", "let2 own kit dig", "let3 art zero"]

아이디어: 여기서는 split하여 우선 [1]이 숫자인지 문자인지 판단한 후 숫자라면 우선 새로운 배열에 넣어준다
        그런데 여기서 이제 만약 [1]이 같다면 [0]을 비교하여 sort해야한다.

"""


def reorderLogFiles(logs: list[str])->list[str]:

    letters, digits = [], []

    #입력 받은 리스트에 대하여 숫자 문자 판별
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    #문자가 동일할 경우 식별자 순으로 정렬하기 위한 코드
    #lambda에 대해서 다시 한 번 봐야햔다.(2022/01/19)
    letters.sort(key=lambda letters: (letters.split()[1:], letters.split())) ## 람다 표현식으로 먼저 문자를 검색 후 index 1에 해당하는 문자가 동일할 시, index 0 번째를 비교하여 sort한다.


    print(list(letters+digits))

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6", "let2 own kit dig", "let3 art zero"]
reorderLogFiles(logs)


