# **题目：**输入一个链表，反转链表后，输出新链表的表头。


# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead is None or pHead.next is None:
            return pHead
        pre = None
        while pHead:
            # 暂存当前节点的下一个节点信息
            temp = pHead.next
            # 反转节点
            pHead.next = pre
            # 进行下一个节点
            pre = pHead
            pHead = temp
        return pre


if __name__ == '__main__':
    solution = Solution()
    p1 = ListNode(1)
    p2 = ListNode(2)
    p3 = ListNode(3)
    p1.next = p2
    p2.next = p3
    ans = solution.ReverseList(p1)
    print(ans.val)
