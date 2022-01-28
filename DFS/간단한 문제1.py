"""
부분 집합 구하기

상태 트리가 뭐냐 -> 재귀를 좀 더 쉽게 이해할 수 있도록 그려보는 것

1. 부분집합이 경우 선택하는 것, 선택하지 않는 것으로 고를 수 있다.

재귀란 탈출조건이 중요한데 이 문제에서는 레벨이 4일 경우에 탈출해야한다.
또하나 중요한 점은 브랜치의 갯수 == 재귀를 호출하는 갯수
2개씩 뻗어가는 것이므로 이 문제에서는 재귀를 2번만 하면 된다.


"""
# def DFS(L,res):
#     if L == len(N):
#         print(res)
#         return
#
#     DFS(L + 1, res + [N[L]])
#     DFS(L + 1, res)
#
#
# N = [4,5,6]
# DFS(0,[])


"""
중복 순열

"""

# # 1,2,3,4를 입력 받기 위한 수 (갯수를 입력 받기 위함)
# N = int(input())
#
# # 전체 갯수 중 뽑아야할 갯수에 대한 입력
# M = int(input())
#
# # DFS 함수로 level과 결과에 해당하는 res가 받아야할 변수로 필요하다.
# # 현재 level은 M에 해당할 것이며
# # 재귀를 실행해야할 횟수 즉 간선의 갯수는 N이다.
# def DFS(L,res):
#     if L == M:
#         print(res)
#         return
#
#     for i in range(N):
#         DFS(L+1, res + str(i+1))
#
#
# DFS(0,[])


######
# N = [4,5,6,7]
#
# # 전체 갯수 중 뽑아야할 갯수에 대한 입력
# M = int(input())
#
# # DFS 함수로 level과 결과에 해당하는 res가 받아야할 변수로 필요하다.
# # 현재 level은 M에 해당할 것이며
# # 재귀를 실행해야할 횟수 즉 간선의 갯수는 N이다.
# def DFS(L,res):
#     if L == M:
#         print(res)
#         return
#
#     for i in range(len(N)):
#         if N[i] in res:
#             continue
#         else:
#             DFS(L+1, res + [N[i]])
#
#
# DFS(0,[])

############################


N = [4,5,6,7]

# 전체 갯수 중 뽑아야할 갯수에 대한 입력
M = int(input())


####### 조합
def DFS(L,res,idx):

    if L == M:
        print(res)
        return

    for i in range(idx+1, len(N)+1):
        DFS(L + 1, res + [N[i]], idx + i)


DFS(0,[],0)







