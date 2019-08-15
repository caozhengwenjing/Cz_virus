# **题目：**给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
#
# **思路：**把链表中节点值放到dict数组中，并记录出现的次数，如果出现次数超过一次，则为环的入口节点。

# -*- coding:utf-8 -*-


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if pHead is None:
            return None
        num, dict, flag = [], {}, True
        tempans = 0
        while pHead and flag == True:
            num.append(pHead.val)
            numset = set(num)
            for c in numset:
                dict[c] = 0
            for c in num:
                dict[c] = dict[c] + 1
            for c in num:
                if dict[c] > 1:
                    flag = False
                    tempans = c
            pHead = pHead.next
        while pHead:
            if pHead.val == tempans:
                return pHead
            pHead = pHead.next
        return None


if __name__ == '__main__':
    pHead1 = ListNode(1)
    pHead2 = ListNode(2)
    pHead3 = ListNode(3)
    pHead4 = ListNode(4)
    pHead5 = ListNode(5)

    pHead1.next = pHead2
    pHead2.next = pHead3
    pHead3.next = pHead4
    pHead4.next = pHead5
    pHead5.next = pHead1

    solution = Solution()
    ans = solution.EntryNodeOfLoop(pHead1)
    print(ans.val)
