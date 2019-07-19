# 题目： 操作给定的二叉树，将其变换为源二叉树的镜像。
# 输入描述：
# ​	源二叉树
# 8
# /
# 6 10
# / \ /
# 5 7 9 11
# 镜像二叉树
# 8
# /
# 10 6
# / \ /
# 11 9 7 5
#
# **思路：**递归实现反转每个子节点

# -*- coding:utf-8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if root is None:
            return
        if root.left is None and root.right is None:
            return
        temp = root.left
        root.left = root.right
        root.right = temp

        if root is not None:
            self.Mirror(root.left)
        if root is not None:
            self.Mirror(root.right)

    def order_traversal(self, root, result):
        if not root:
            return
        self.order_traversal(root.left, result)
        result.append(root.val)
        self.order_traversal(root.right, result)


if __name__ == '__main__':
    A1 = TreeNode(8)
    A2 = TreeNode(6)
    A3 = TreeNode(10)
    A4 = TreeNode(5)
    A5 = TreeNode(7)
    A6 = TreeNode(9)
    A7 = TreeNode(11)
    A1.left = A2
    A1.right = A3
    A2.left = A4
    A2.right = A5
    A3.left = A6
    A3.right = A7

    temp1 = []
    solution = Solution()
    solution.order_traversal(A1, temp1)
    print(temp1)
    solution.Mirror(A1)
    solution.order_traversal(A1, temp1)
    print(temp1)
