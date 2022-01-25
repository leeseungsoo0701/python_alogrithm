"""
이진트리의 최대 깊이를 구하라.
[3,9,20,null,null,15,7이 구해질 때]
깊이는 3이다.


아이디어:
이진트리의 구성을 보면 완전 이진트리로 깊이를 구하기 위해서는 둘 중 하나라도 계속 노드가 리프까지 갈 수 있도록
while 안에서 돌려주고 그 다음 한 바퀴 돌 때마다 cnt +1 해준다

"""

from collections import deque
from idlelib.tree import TreeNode


count = 0
def maxDepth(root:TreeNode)-> int:
    global count

    queue = deque([root])

    while queue:
        count +=1

        for _ in range(len(queue)):
            front = queue.popleft()
            if front.left:
                queue.append(front.left)
            if front.right:
                queue.append(front.right)


    return count



















# from collections import deque
# from idlelib.tree import TreeNode
#
# def maxDepth(self, root: TreeNode) -> int:
#     if root is None:
#         return 0
#
#     queue = deque([root])
#     depth = 0
#
#     while queue:
#         depth += 1
#
#         for _ in range(len(queue)):
#             cur_root = queue.popleft()
#
#             if cur_root.left:
#                 queue.append(cur_root.left)
#             if cur_root.right:
#                 queue.append(cur_root.right)
#
#     return depth
