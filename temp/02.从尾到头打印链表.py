# **题目：**输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
#
# **思路：**将链表中的值记录到list之中，然后进行翻转list。

# -*- coding:utf-8 -*-


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        l = []
        while listNode:
            l.append(listNode.val)
            listNode = listNode.next
        return l[::-1]



if __name__ == '__main__':
    A1 = ListNode(1)
    A2 = ListNode(2)
    A3 = ListNode(3)
    A4 = ListNode(4)
    A5 = ListNode(5)

    A1.next = A2
    A2.next = A3
    A3.next = A4
    A4.next = A5

    solution = Solution()
    ans = solution.printListFromTailToHead(A1)
    print(ans)
