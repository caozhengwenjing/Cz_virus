# **题目：**用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
#
# **题解：**申请两个栈Stack1和Stack2，Stack1当作输入，Stack2当作pop。当Stack2空的时候，将Stack1进行反转，并且输入到Stack2。

# -*- coding:utf-8 -*-


class Solution:
    def __init__(self):
        self.Stack1 = []
        self.Stack2 = []

    def push(self, node):
        # write code here
        self.Stack1.append(node)

    def pop(self):
        # return xx
        if self.Stack2 == []:
            while self.Stack1:
                self.Stack2.append(self.Stack1.pop())
            return self.Stack2.pop()
        return self.Stack2.pop()


if __name__ == '__main__':
    solution = Solution()
    solution.push(1)
    solution.push(2)
    solution.push(3)
    print(solution.pop())
