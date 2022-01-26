"""
동일한 값을 지닌 가장 긴 경로를 찾아라.

[5,4,5,1,1,NULL,5]

아이디어:


"""
from idlelib.tree import TreeNode


class Solution:
    result : int = 0

    def longstUnivalue(self, root : TreeNode )->int:
        def dfs(node : TreeNode):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if node.left.val == node.val:
                left += 1
            else:
                left = 0

            if node.right.val ==node.val:
                right +=1
            else:
                right = 0

            self.result = max(self.result, left + right)

            return max(left, right)

        dfs(root)
        return self.result


################################################
class Solution:
    result : int = 0

    def longstUnivalue(self, root : TreeNode )->int:
        def dfs(node : TreeNode):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0

            if node.right and node.right.val ==node.val:
                right +=1
            else:
                right = 0

            self.result = max(self.result, left+right)

            return max(left,right)


        dfs(root)
        return self.result
