# **题目：**从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        root=pRoot
        if not root:
            return []
        level=[root]
        result=[]
        while level:
            curvalues=[]
            nextlevel=[]
            for i in level:
                curvalues.append(i.val)
                if i.left:
                    nextlevel.append(i.left)
                if i.right:
                    nextlevel.append(i.right)
            if curvalues:
                    result.append(curvalues)
            level = nextlevel
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
