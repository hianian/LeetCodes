"""
给你一个字符串 s，找到 s 中最长的回文子串。

    示例 1：

        输入：s = "babad"
        输出："bab"
        解释："aba" 同样是符合题意的答案。
    示例 2：

        输入：s = "cbbd"
        输出："bb"
    示例 3：

        输入：s = "a"
        输出："a"
    示例 4：

        输入：s = "ac"
        输出："a"
 

    提示：

        1 <= s.length <= 1000
        s 仅由数字和英文字母（大写和/或小写）组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


"""
    这道题没做出来，参考了网上的解题思路
"""

"""
    思路1：
        暴力破解，就枚举找出所有的子串，依次判断每个字符串即可
        可惜结果超时
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:

        # 因为长度最低为1，所以，如果没有回文串，就认为第一个字符是回文子串。
        result = s[0]

        for start in range(len(s)):
            for end in range(start, len(s)):
                tempStart = start
                tempEnd = end
                for i in range((tempEnd - tempStart + 1) // 2):
                    if s[tempStart] != s[tempEnd]:
                        break
                    tempStart += 1
                    tempEnd -= 1
                else:
                    if len(result) < end - start + 1:
                        # print(end, start)
                        result = s[start: end + 1]

        return result



if __name__ == '__main__':
    # s = "abcbabcba"
    # s = "abaefdeedf"
    # s = "ac"
    # s = "a"
    # s = "cbbd"
    # s = "babad"
    s = "bb"
    sol_1 = Solution()

    print(sol_1.longestPalindrome(s))

