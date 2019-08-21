# **题目：**请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，
#         第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
#
# 思路： 把当前列结果存放到list之中，设置翻转变量，依次从左到右打印和从右到左打印。

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        root=pRoot
        if not root:
            return []
        level=[root]
        result=[]
        righttoleft=False
        while level:
            curvalues=[]
            nextlevel=[]
            for i in level:
                curvalues.append(i.val)
                if i.left:
                    nextlevel.append(i.left)
                if i.right:
                    nextlevel.append(i.right)
            if righttoleft:
                    curvalues.reverse()
            if curvalues:
                    result.append(curvalues)
            level = nextlevel
            righttoleft = not righttoleft
        return result

if __name__=='__main__':
    A1 = TreeNode(1)
    A2 = TreeNode(2)
    A3 = TreeNode(3)
    A4 = TreeNode(4)
    A5 = TreeNode(5)
    A6 = TreeNode(6)
    A7 = TreeNode(7)

    A1.left=A2
    A1.right=A3
    A2.left=A4
    A2.right=A5
    A3.left=A6
    A3.right=A7

    solution = Solution()
    ans=solution.Print(A1)
    print(ans)

