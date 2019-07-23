# **题目：**输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，
#                 另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。
#                 （注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）。
#
# **思路：**将大问题转变为小问题，每次都进行复制头部节点，然后进行递归，每次同样处理头部节点。

# -*- coding:utf-8 -*-


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        # 复制头部节点
        if pHead is None:
            return None

        newHead = RandomListNode(pHead.label)
        newHead.next = pHead.next
        newHead.random = pHead.random

        # 递归其他节点
        newHead.next = self.Clone(pHead.next)

        return newHead


if __name__ == '__main__':
    A1 = RandomListNode(2)
    A2 = RandomListNode(3)
    A3 = RandomListNode(4)
    A4 = RandomListNode(5)
    A5 = RandomListNode(6)

    A1.next = A2
    A1.random = A3

    A2.next = A3
    A2.random = A4

    A3.next = A4
    A3.random = A5

    A4.next = A5
    A4.random = A3

    solution = Solution()
    ans = solution.Clone(A1)
