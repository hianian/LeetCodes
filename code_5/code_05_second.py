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
    思路2：
        中心扩散法
        就是遍历每一个索引，以这个索引为中心，然后利用“回文串”的特性，尽可能多的向两侧扩散，看最多能扩散多远。
"""


class Solution:

    def getSubString(self, s, start, end):

        while start >= 0 and end < len(s):
            if s[start] != s[end]:
                break
            start -= 1
            end += 1

        # 注意，此时无论是break跳出循环，还是while条件不满足，都是此时 s[start] != s[end]，所以都是上一次的s[start] == s[end]
        start += 1
        end -= 1
        return s[start:end + 1]

    def longestPalindrome(self, s: str) -> str:

        result = s[0]

        # 遍历字符串，将每个字符都作为中心点判断一下。（注意，如果中心点是最后一个，则没有必要判断了）
        for indexCenter in range(0, len(s) - 1):

            # TODO, 那么如何判断这两种情况呢？（目前没办法判断，只能是把两种情况分别判断一下，看看哪个回文串的长度比较长）
            # 有两种情况，一种是回文子串的长度是奇数；
            # 奇数的情况，中心点就是一个，所以两侧直接延伸即可
            oddString = self.getSubString(s, indexCenter, indexCenter)

            # 一种是回文子串的长度是偶数（这种情况是对称的，也就是中心点不是一个）
            # 这种情况，就需要将此时的下标以及下标的下一个当做中心点，然后两侧延伸。
            evenString = self.getSubString(s, indexCenter, indexCenter + 1)

            if len(oddString) < len(evenString):
                if len(result) < len(evenString):
                    result = evenString
            else:
                if len(result) < len(oddString):
                    result = oddString

        return result


if __name__ == '__main__':
    # s = "abcbabcba"
    # s = "abaefdeedf"
    # s = "ac"
    # s = "a"
    # s = "cbbd"
    # s = "babad"
    s = "bb"
    sol_2 = Solution()

    print(sol_2.longestPalindrome(s))

