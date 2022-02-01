"""
aabbaccc

ababcdcdababcdcd
"""
# 문자열 입력 받기
s = input()
answer = 100000

# 최대 비교는 전체 길이의 반까지만 해주면 되기에 1~len(s)//2+1 까지 진행하면 된다.
for step in range(1, (len(s)//2+1)+1):
    res = ''
    count = 1
    temp = s[:step]

    for j in range(step, len(s)+step, step):
        if temp == s[j:j + step]:
            count += 1
        else:
            if count == 1:
                res += temp
            else:
                res += str(count) + temp

            temp = s[j:j + step]
            count = 1

    answer = min(answer, len(res))

print(answer)




