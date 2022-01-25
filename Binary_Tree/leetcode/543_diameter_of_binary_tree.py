"""
이진트리에서 두 노드간 가장 긴 경로의 길이를 출력하라.

[1,2,3,4,5,Null,Null]

"""


from idlelib.tree import TreeNode


class Solutions:
    longest: int = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node: TreeNode):
            if not node:
                return -1

            left = dfs(node.left)
            right = dfs(node.right)

            self.longest = max(self.longest, left + right + 2)

            return max(left, right) + 1

        dfs(root)
        return self.longest
