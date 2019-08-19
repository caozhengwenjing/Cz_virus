# **题目：**请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。

# **思路：**采用递归的方法来判断两数是否相同。
# -*- coding:utf-8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot:
            return True
        result = self.same(pRoot, pRoot)
        return result

    def same(self, root1, root2):
        if not root1 and not root2:
            return True
        if root1 and not root2:
            return False
        if not root1 and root2:
            return False
        if root1.val != root2.val:
            return False

        left = self.same(root1.left, root2.right)
        if not left:
            return False
        right = self.same(root1.right, root2.left)
        if not right:
            return False
        return True


if __name__ == '__main__':
    A1 = TreeNode(1)
    A2 = TreeNode(2)
    A3 = TreeNode(2)
    A4 = TreeNode(3)
    A5 = TreeNode(4)
    A6 = TreeNode(4)
    A7 = TreeNode(3)

    A1.left = A2
    A1.right = A3
    A2.left = A4
    A2.right = A5
    A3.left = A6
    A3.right = A7

    solution = Solution()
    ans = solution.isSymmetrical(A1)
    print(ans)
