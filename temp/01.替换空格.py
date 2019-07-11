# class Solution:
#     # s 源字符串
#     def replaceSpace(self, s):
#         # write code here
#         temp = s.replace(" ", "%20")
#         return temp
#
#
# if __name__ == '__main__':
#     s = 'We Are Happy'
#     solution = Solution()
#     ans = solution.replaceSpace(s)
#     print(ans)


class Solution:
    def replaceSpace(self, s):
        temp = s.replace(" ", "%20")
        return temp


if __name__ == '__main__':
    s = "we are bim"
    solution = Solution()
    ans = solution.replaceSpace(s)
    print(ans)


class Solution:
    def repalpPlcw(self, s):
        temp = s.replace(" ", "%9")
        return temp


if __name__ == '__main__':
    s = "project and prejenct"
    an = Solution().repalpPlcw(s)
    print(an)


