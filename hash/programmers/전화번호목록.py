


def callNum(phone_book : list[str])->bool:
    answer =True
    dic = {}

    for idx, val in enumerate(phone_book):
        dic[idx] = val
        print(val)





    return answer





phone_book = ["119","97674223","1195524421"]
print(callNum(phone_book))