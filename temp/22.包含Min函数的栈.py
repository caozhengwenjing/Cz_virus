# **题目：**定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数。

# -*- coding:utf-8 -*-


class Solution:
    def __init__(self):
        self.num = []

    def push(self, node):
        # write code here
        self.num.append(node)

    def pop(self):
        # write code here
        self.num.pop()

    def top(self):
        # write code here
        numlen = len(self.num)
        return self.num[numlen - 1]

    def min(self):
        # write code here
        return min(self.num)


if __name__ == '__main__':
    solution = Solution()
    solution.push(1)
    solution.push(2)
    solution.push(3)
    solution.push(4)
    solution.pop()
    print(solution.top())
    print(solution.min())
