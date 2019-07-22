# **题目：**输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
#           如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
#
# **思路：**二叉搜索树的特性是所有左子树值都小于中节点，所有右子树的值都大于中节点，
#               递归遍历左子树和右子树的值。

# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        if len(sequence) == 1:
            return True
        i = 0
        while sequence[i] < sequence[-1]:
            i = i + 1
        k = i
        for j in range(i, len(sequence) - 1):
            if sequence[j] < sequence[-1]:
                return False

        leftsequence = sequence[:k]
        rightsequence = sequence[k:len(sequence) - 1]

        leftans = True
        rightans = True

        if len(leftsequence) > 0:
            self.VerifySquenceOfBST(leftsequence)
        if len(rightsequence) > 0:
            self.VerifySquenceOfBST(rightsequence)

        return leftans and rightans


if __name__ == '__main__':
    solution = Solution()
    num = list(map(int, input().split(' ')))
    ans = solution.VerifySquenceOfBST(num)
    print(ans)
