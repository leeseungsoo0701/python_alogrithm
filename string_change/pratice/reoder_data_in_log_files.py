##################### 로그를 재정렬하라 기준은 다음과 같다.
##################### 1. 로그의 가장 앞 부분은 식별자이다.
#################### 2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
##################### 3. 식별자는 순서에 영향을 끼치진 않지만, 문자가 동일할 경우 식별자 순으로한다
################# 4. 숫자 로그는 순서대로 한다.
############### 입력 : logs = ['dig1 8 1 5 1","let1 art can","dig2 3 6", "let2 own kit dig", "let3 art zero"]

def reorderLogFiles(logs: list[str])->list[str]:
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
    letters.sort(key=lambda letters: (letters.split()[1:], letters.split())) ## 람다 표현식으로 먼저 문자를 검색 후 index 1에 해당하는 문자가 동일할 시, index 0 번째를 비교하여 sort한다.
    print(list(letters+digits))

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6", "let2 own kit dig", "let3 art zero"]
reorderLogFiles(logs)


