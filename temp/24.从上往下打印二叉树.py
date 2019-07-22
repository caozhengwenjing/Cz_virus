# **题目：**从上往下打印出二叉树的每个节点，同层节点从左至右打印。
#
# **思路：**递归，每次将左子树结果和右子树结果存到结果集之中。

# -*- coding:utf-8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if root is None:
            return []
        ans = []
        ans.append(root.val)
        self.orderans(root, ans)
        return ans

    def orderans(self, root, ans):
        if not root:
            return
        if root.left:
            ans.append(root.left.val)
        if root.right:
            ans.append(root.right.val)

        self.orderans(root.left, ans)
        self.orderans(root.right, ans)


if __name__ == '__main__':
    solution = Solution()
    A1 = TreeNode(1)
    A2 = TreeNode(2)
    A3 = TreeNode(3)
    A4 = TreeNode(4)
    A5 = TreeNode(5)

    A1.left = A2
    A1.right = A3
    A2.left = A4
    A2.right = A5
    ans = solution.PrintFromTopToBottom(A1)
    print(ans)
