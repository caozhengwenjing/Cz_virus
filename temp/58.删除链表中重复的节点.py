# **题目：**在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
#                             例如，链表1->2->3->3->4->4->5 处理后为 1->2->5。
#
# **思路：**记录链表中出现的数字，然后构建新链表。

# -*- coding:utf-8 -*-


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        num = []
        tempnum1 = pHead
        while tempnum1:
            num.append(tempnum1.val)
            tempnum1 = tempnum1.next
        dict = {}
        for c in num:
            dict[c] = 0
        for c in num:
            dict[c] = dict[c] + 1
        newnum = []
        for c in num:
            if dict[c] == 1:
                newnum.append(c)
        if newnum == []:
            return None
        head = ListNode(newnum[0])
        temphead = head
        for i in range(1, len(newnum)):
            tempnode = ListNode(newnum[i])
            temphead.next = tempnode
            temphead = tempnode
        # while head:
        #     print(head.val)
        #     head=head.next
        return head


if __name__ == '__main__':
    pHead1 = ListNode(1)
    pHead2 = ListNode(1)
    pHead3 = ListNode(1)
    pHead4 = ListNode(1)
    pHead5 = ListNode(1)
    pHead6 = ListNode(1)
    pHead7 = ListNode(1)

    pHead1.next = pHead2
    pHead2.next = pHead3
    pHead3.next = pHead4
    pHead4.next = pHead5
    pHead5.next = pHead6
    pHead6.next = pHead7

    solution = Solution()
    ans = solution.deleteDuplication(pHead1)
    print(ans)
