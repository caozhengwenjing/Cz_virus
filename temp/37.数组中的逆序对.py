# **题目描述：**在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
#           输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007。
#
# **输入描述：**题目保证输入的数组中没有的相同的数字。
#
# 数据范围：
# 对于%50的数据,size<=10^4
# 对于%75的数据,size<=10^5
# 对于%100的数据,size<=2*10^5
#
# 示例1
# 输入 1,2,3,4,5,6,7,0
# 输出 7

# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # write code here
        global count
        count = 0

        def A(array):
            global count
            if len(array) <= 1:
                return array
            k = int(len(array) / 2)
            left = A(array[:k])
            right = A(array[k:])
            l = 0
            r = 0
            result = []
            while l < len(left) and r < len(right):
                if left[l] < right[r]:
                    result.append(left[l])
                    l += 1
                else:
                    result.append(right[r])
                    r += 1
                    count += len(left) - l
            result += left[l:]
            result += right[r:]
            return result

        A(data)
        return count % 1000000007


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 7, 0]
    solution = Solution()
    ans = solution.InversePairs(data)
    print(ans)
