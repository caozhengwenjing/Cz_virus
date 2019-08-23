# **题目：**请实现两个函数，分别用来序列化和反序列化二叉树。
#
# **思路：**转变成前序遍历，空元素利用"#"代替，然后进行解序列。
# -*- coding:utf-8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import collections


class Solution:
    def Serialize(self, root):
        # write code here
        if not root:
            return None
        res = []
        self.pre(root, res)
        return res

    def pre(self, root, res):
        if not root:
            return
        res.append(root.val)
        if root.left:
            self.pre(root.left, res)
        else:
            res.append('#')
        if root.right:
            self.pre(root.right, res)
        else:
            res.append('#')

    def Deserialize(self, s):
        if s == '':
            return None
        vals = []
        for i in range(0, len(s)):
            vals.append(s[i])
        vals = collections.deque(vals)
        ans = self.build(vals)
        return ans

    def build(self, vals):
        if vals:
            val = vals.popleft()
            if val == '#':
                return None
            root = TreeNode(int(val))
            root.left = self.build(vals)
            root.right = self.build(vals)
            return root
        return self.build(vals)


# [1, ',', 2, ',', 4, ',', ',', ',', 5, ',', ',', ',', 3, ',', 6, ',', ',', ',', 7, ',', ',']
if __name__ == "__main__":
    A1 = TreeNode(1)
    A2 = TreeNode(2)
    A3 = TreeNode(3)
    A4 = TreeNode(4)
    A5 = TreeNode(5)
    A6 = TreeNode(6)
    A7 = TreeNode(7)

    A1.left = A2
    A1.right = A3
    A2.left = A4
    A2.right = A5
    A3.left = A6
    A3.right = A7

    solution = Solution()
    ans = solution.Serialize(A1)
    print(ans)
    root = solution.Deserialize(ans)
    res = solution.Serialize(root)
    print(res)
