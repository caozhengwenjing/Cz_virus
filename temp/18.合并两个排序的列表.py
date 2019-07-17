# **题目：**输入两个单调递增的链表，输出两个链表合成后的
#         链表，当然我们需要合成后的链表满足单调不减规则。
#
# # **题解：**将两个链表之中的数值转换到列表之中，
# #           并进行排序，将排序后的列表构造成链表。

# -*- coding:utf-8 -*-


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 is None and pHead2 is None:
            return None
        num1, num2 = [], []
        while pHead1:
            num1.append(pHead1.val)
            pHead1 = pHead1.next
        while pHead2:
            num2.append(pHead2.val)
            pHead2 = pHead2.next
        ans = num1 + num2
        ans.sort()
        head = ListNode(ans[0])
        pre = head
        for i in range(1, len(ans)):
            node = ListNode(ans[i])
            pre.next = node
            pre = pre.next
        return head


if __name__ == '__main__':
    solution = Solution()
    pHead1_1 = ListNode(1)
    pHead1_2 = ListNode(3)
    pHead1_3 = ListNode(5)
    pHead1_1.next = pHead1_2
    pHead1_2.next = pHead1_3

    pHead2_1 = ListNode(2)
    pHead2_2 = ListNode(4)
    pHead2_3 = ListNode(6)
    pHead2_1.next = pHead2_2
    pHead2_2.next = pHead2_3
    ans = solution.Merge(pHead1_1, pHead2_1)
    print(ans.val)
