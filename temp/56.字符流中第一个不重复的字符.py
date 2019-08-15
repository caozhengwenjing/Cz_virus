# **题目：**请实现一个函数用来找出字符流中第一个只出现一次的字符。
#         例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。
#             当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
#
# **输出描述：**如果当前字符流没有存在出现一次的字符，返回#字符。
# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.all={}
        self.ch=[]
    def FirstAppearingOnce(self):
        # write code here
        if self.all is None:
            return '#'
        for c in self.ch:
            if self.all[c]==1:
                return c
        return '#'

    def Insert(self, char):
        # write code here
        self.ch.append(char)
        if char in self.all:
            self.all[char]=self.all[char]+1
        else:
            self.all[char]=1

if __name__=='__main__':
    solution=Solution()
    solution.Insert('g')
    ans = solution.FirstAppearingOnce()
    print(ans)
    solution.Insert('o')
    ans = solution.FirstAppearingOnce()
    print(ans)
    solution.Insert('o')
    ans = solution.FirstAppearingOnce()
    print(ans)
    solution.Insert('g')
    ans = solution.FirstAppearingOnce()
    print(ans)
    solution.Insert('l')
    ans = solution.FirstAppearingOnce()
    print(ans)
    solution.Insert('e')
    ans = solution.FirstAppearingOnce()
    print(ans)
