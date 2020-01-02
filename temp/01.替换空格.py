class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        temp = s.replace(" ", "%20")
        return temp




if __name__ == '__main__':
    s = 'We Are Happy'
    solution = Solution()
    ans = solution.replaceSpace(s)
    print(ans)
