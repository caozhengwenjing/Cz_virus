# **题目：**在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1。

# **思路：**找出所有出现一次的字符，然后进行遍历找到第一次出现字符的位置。

# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if not s:
            return -1
        sset = set(s)
        dict = {}
        for c in sset:
            dict[c] = 0
        for i in range(0, len(s)):
            dict[s[i]] = dict[s[i]] + 1
        onetime = []
        for c in dict:
            if dict[c] == 1:
                onetime.append(c)

        if onetime is None:
            return -1
        else:
            index = 0
            for i in range(0, len(s)):
                if s[i] in onetime:
                    index = i
                    break
            return index


if __name__ == '__main__':
    s = 'rray'
    solution = Solution()
    ans = solution.FirstNotRepeatingChar(s)
    print(ans)
