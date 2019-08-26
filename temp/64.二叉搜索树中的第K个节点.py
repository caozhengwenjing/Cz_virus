# **题目：**给定一棵二叉搜索树，请找出其中的第k小的结点。例如（5，3，7，2，4，6，8）中，
#             按结点数值大小顺序第三小结点的值为4。
#
# **思路：**中序遍历后，返回第K个节点值。

# -*- coding:utf-8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        res = []
        if not pRoot:
            return None
        self.order(pRoot, res)
        if len(res) < k or k <= 0:
            return None
        else:
            return res[k - 1]

    def order(self, root, res):
        if not root:
            return
        self.order(root.left, res)
        res.append(root)
        self.order(root.right, res)


if __name__ == '__main__':
    A1 = TreeNode(5)
    A2 = TreeNode(3)
    A3 = TreeNode(7)
    A4 = TreeNode(2)
    A5 = TreeNode(4)
    A6 = TreeNode(6)
    A7 = TreeNode(8)

    A1.left = A2
    A1.right = A3
    A2.left = A4
    A2.right = A5
    A3.left = A6
    A3.right = A7

    k = 3
    solution = Solution()
    ans = solution.KthNode(A1, k)
    print(ans)
