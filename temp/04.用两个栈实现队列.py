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
