# **题目：**输入一棵二叉树，判断该二叉树是否是平衡二叉树。
#
# **题解：**平衡二叉树是左右子数的距离不能大于1，因此递归左右子树，判断子树距离是否大于1。

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if pRoot is None:
            return True
        if abs(self.TreeDepth(pRoot.left) - self.TreeDepth(pRoot.right)) > 1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)

    def TreeDepth(self, root):
        if root is None:
            return 0
        left = self.TreeDepth(root.left)
        right = self.TreeDepth(root.right)
        return max(left + 1, right + 1)


if __name__ == '__main__':
    A1 = TreeNode(1)
    A2 = TreeNode(2)
    A3 = TreeNode(3)
    A4 = TreeNode(4)
    A5 = TreeNode(5)
    A6 = TreeNode(6)

    A1.left = A2
    A1.right = A3
    A2.left = A4
    A2.right = A5
    # A4.left=A6

    solution = Solution()
    ans = solution.IsBalanced_Solution(A1)
    print(ans)
