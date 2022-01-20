"""
문제 : 세계는 균형이 잘 잡혀있어야 한다. 양과 음, 빛과 어둠 그리고 왼쪽 괄호와 오른쪽 괄호처럼 말이다.

정민이의 임무는 어떤 문자열이 주어졌을 때, 괄호들의 균형이 잘 맞춰져 있는지 판단하는 프로그램을 짜는 것이다.

문자열에 포함되는 괄호는 소괄호("()") 와 대괄호("[]")로 2종류이고, 문자열이 균형을 이루는 조건은 아래와 같다.

모든 왼쪽 소괄호("(")는 오른쪽 소괄호(")")와만 짝을 이뤄야 한다.
모든 왼쪽 대괄호("[")는 오른쪽 대괄호("]")와만 짝을 이뤄야 한다.
모든 오른쪽 괄호들은 자신과 짝을 이룰 수 있는 왼쪽 괄호가 존재한다.
모든 괄호들의 짝은 1:1 매칭만 가능하다. 즉, 괄호 하나가 둘 이상의 괄호와 짝지어지지 않는다.
짝을 이루는 두 괄호가 있을 때, 그 사이에 있는 문자열도 균형이 잡혀야 한다.
정민이를 도와 문자열이 주어졌을 때 균형잡힌 문자열인지 아닌지를 판단해보자.


입력: 하나 또는 여러줄에 걸쳐서 문자열이 주어진다. 각 문자열은 영문 알파벳, 공백, 소괄호("( )") 대괄호("[ ]")등으로 이루어져 있으며, 길이는 100글자보다 작거나 같다.

입력의 종료조건으로 맨 마지막에 점 하나(".")가 들어온다.


출력: 각 줄마다 해당 문자열이 균형을 이루고 있으면 "yes"를, 아니면 "no"를 출력한다.

"""

# dic = {
#     "}": "{",
#     ")": "("
#     }
#
# opener = "({"
#
# total = "(){}"
#
#
#
# answer = []
#
#
# while True:
#     words = input()
#     stack_1 = []
#     result = []
#
#     if words == ".":
#         break
#
#     for word in words:
#         if word in total:
#             stack_1.append(word)
#         else:
#             pass
#
#
#
#     for val in stack_1:
#         if val in opener:
#             result.append(val)
#         else:
#             if dic[val] != stack_1.pop():
#                 answer.append(1)
#                 break
#             else:
#                 answer.append(0)
#
#
#         # if word in opener:
#         #     stack.append(word)
#         #
#         # elif word not in total:
#         #     pass
#         #
#         # elif stack:
#         #     if dic[word] != stack.pop():
#         #         answer = False
#
# # for i in answer:
# #     if i == 0:
# #         print("yes")
# #     else:
# #         print("no")
#
#
#
# print(count)
# for i in range(count-1):
#     if 1 in answer:
#         print("no")
#     else:
#         print("yes")



# #############################
# import sys
#
#
#
# stack = []
#
#
# while True:
#     strs = sys.stdin.readline().rstrip('.')
#
#     if strs == ".":
#         break
#
#
#     for char in strs:
#         if char.isalnum() or char == " ":
#             continue
#
#         if char == "(" or char == "[":
#             stack.append(char)
#             continue
#         if char == ")":
#             if stack and stack[-1] == "(":
#                 stack.pop()
#                 continue
#             else:
#                 print("no")
#                 break
#         if char == "]":
#             if stack and stack[-1] == "[":
#                 stack.pop()
#                 continue
#             else:
#                 print("no")
#                 break
#
#     print("yes")




#######################
while True :
    a = input()
    stack = []

    if a == "." :
        break

    for i in a :
        if i == '[' or i == '(' :
            stack.append(i)
        elif i == ']' :
            if len(stack) != 0 and stack[-1] == '[' :
                stack.pop() # 맞으면 지워서 stack을 비워줌 0 = yes
            else :
                stack.append(']')
                break
        elif i == ')' :
            if len(stack) != 0 and stack[-1] == '(' :
                stack.pop()
            else :
                stack.append(')')
                break
    if len(stack) == 0 :
        print('yes')
    else :
        print('no')
