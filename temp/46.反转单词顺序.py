# **题目：**牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志，写些句子在本子上。
# 同事Cat对Fish写的内容颇感兴趣，有一天他向Fish借来翻看，但却读不懂它的意思。例如，“student. a am I”。
# 后来才意识到，这家伙原来把句子单词的顺序翻转了，正确的句子应该是“I am a student.”。

# -*- coding:utf-8 -*-


class Solution:
    def ReverseSentence(self, s):
        # write code here
        ans, word = [], ''
        for i in range(0, len(s)):
            word = word + s[i]
            if s[i] == ' ':
                ans.append(word)
                word = ''
            if i == len(s) - 1:
                word = word + ' '
                ans.append(word)
        ans.reverse()
        res = ''
        for c in ans:
            res = res + c
        return res[:len(res) - 1]


if __name__ == '__main__':
    solution = Solution()
    s = 'I am a student.'
    ans = solution.ReverseSentence(s)
    print(ans)
