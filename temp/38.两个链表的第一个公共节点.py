# **题目：**输入两个链表，找出它们的第一个公共结点。

# -*- coding:utf-8 -*-


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        list1 = []
        list2 = []
        node1 = pHead1
        node2 = pHead2
        while node1:
            list1.append(node1.val)
            node1 = node1.next
        while node2:
            if node2.val in list1:
                return node2
            else:
                node2 = node2.next


if __name__ == '__main__':
    A1 = ListNode(1)
    A2 = ListNode(2)
    A3 = ListNode(3)
    A1.next = A2
    A2.next = A3

    B4 = ListNode(4)
    B5 = ListNode(5)
    B4.next = B5

    C6 = ListNode(6)
    C7 = ListNode(7)

    A3.next = C6
    B5.next = C6
    C6.next = C7

    solution = Solution()
    ans = solution.FindFirstCommonNode(A1, B4)
    print(ans.val)
