#################################
def long_panlindromic(str):
    isPalin = True


    #i+j = len(str)-1
    for i in range(len(str) // 2, len(str)):
        while isPalin:
            j = len(str)-i-1
            if str[i] != str[j]:
                print(str[j + 1:i])
                isPalin = False
            elif str[0] == str[len(str)-1]:
                print(str)
                break

# 문자열이 모두 다 같은 경우



long_panlindromic("babad")

#######################################
