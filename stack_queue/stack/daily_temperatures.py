###매일의 화씨 온도 리스트 T를 입력 받아서, 더 따뜻한 날씨를 위해서는 며칠을 더 기다려야하는지 출력하라.
##### 입력 T = [73,74,75,71,69,72,76,73]
##### 출력 [1,1,4,2,1,1,0,0]
##### 1.현재 인덱스를 값을 stack에 넣는다.
##### 2.그 뒤의 배열을 넣는다 (언제? 현재 인덱스보다 온도가 낮을 시, 이떄 count도 늘려준다)
##### 3.현재의 값보다 큰 값이 나올 때, stack을 초기화 시켜주면서 count를 새로운 리스트에 넣어준다(같은 인덱스 값)


# def is_warm(warms : list[int]) -> list[int]:
#     stack = Stack()
#     result_list = [0]*(len(warms)) ### while 문에 한번도 안들어가면 더 따듯해질 날이 없으므로 0의 리스트들을 만들고 그 위에 덮어씌우자
#
#     # cp_warms = warms
#     # cp_warms.append(0)
#
#     for i, warm in enumerate(warms):
#         stack.push(i)   #### 73 들어감
#         while warm < warms[right]:
#             stack.push(right)
#             right +=1
#
#         stack.pop(right)
#
#         result_list[i] = (right - i)
#
#     print(result_list)

######################
def dailyT(T: list[int]) -> list[int]:
    answer = [0]*len(T)    # default를 해주기 위한 0 리스트를 생성
    stack = []             # 인덱스를 넣어줘서 비교하기 위한 value를 비교하기 위한 stack

    for i, warm in enumerate(T):
        ### while stack은 stack에 아무것도 없을 때, 즉 지금의 경우에는 맨 처음에 넣어주는 것을 걸러주기 위한 것이고
        ### warm > T[stack[-1]]에 해당하는 부분은 stack의 top 위치의 value와 현재 값을 비교하여 현재 값이 더 높다면 기존 것들을 pop하고 index끼리 빼주어 그 작은 것들의 위치에 넣어준다.
        while stack and warm > T[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last


        stack.append(i)

    return answer

T = [73, 74, 75, 71, 69, 72, 76, 73]
print(dailyT(T))