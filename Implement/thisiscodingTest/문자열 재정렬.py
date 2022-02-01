# 전체 입력 받는 문자
words = input()

# 문자만 따로 담아두기 위한 리스트
alp = []
total = 0

#for문을 통한 문자와 숫자 구별
for word in words:
    if word.isalpha():
        alp.append(word)
    else:
        total += int(word)

#alp 정렬
alp.sort()

#문자열 정렬 후 더한 total 붙여주기
alp.append(str(total))

# 리스트를 문자열로 보여주기 위한 코드
print("".join(alp))