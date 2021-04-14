"""
    思路3：
        参考其他人的回答
        本来开始没有读懂，后来自己在思路1的方法上修改，修改完之后，对比思路2和本方法
        发现原来二者其实是一样的。

        简单记录一下，代码很简便
"""


class Solution:
    def lengthOfLongestSubstring(self, s):

        st = {}
        i, ans = 0, 0
        for j in range(len(s)):
            if s[j] in st:
                i = max(st[s[j]], i)
            ans = max(ans, j - i + 1)
            st[s[j]] = j + 1
        return ans


if __name__ == '__main__':

    # strs = "abcabcbb"
    # strs = "bbbbbb"
    # strs = "pwwkew"
    # strs = ""
    # strs = " "
    # strs = "abcde"
    # strs = "dvdf"
    # strs = "cdd"
    # strs = "abba"
    strs = "nfpdmpi"

    sol = Solution()

    maxLen = sol.lengthOfLongestSubstring(strs)

    print(maxLen)

