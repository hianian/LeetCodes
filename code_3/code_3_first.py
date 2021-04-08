"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例1：
    输入: s = "abcabcbb"
    输出: 3
    解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例2：
    输入: s = "bbbbb"
    输出: 1
    解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例3：
    输入: s = "pwwkew"
    输出: 3
    解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
         请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

示例4：
    输入: s = ""
    输出: 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
    思路1：
        遍历字符串，每遍历一个字符，就会判断之前是否出现过这个字符。如果没有出现，则把它加入到字典中，
        如果出现了重复字符，那么就把字典中存在的该字符以及其之前的字符都去掉，并把当前字符加入进去。（注意记录最大长度）
        
        比如“dvdf”，首先遍历d，因为字典开始是空，所以直接将d加入到字典中，接着是v；然后到d的时候，因为字典中已经有了d了，
        所以就把d以及d之前的（空）所有字符都去掉，然后长度从v开始计算，即vdf，长度为3。
        
        比如“abcabcbb”，刚开始逐步遍历到abc，此时长度为3，接着当遍历a时，因为已经出现了，所以就把a以及之前的删掉，此时就是bca，
        然后遍历b，将之前的b删掉，此时就是cab，然后是abc，bc，cb，b。但是最长的仍然是3.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}

        # 保存最大长度值
        maxLen = 0

        # 保存临时的最大长度值
        tempLen = 0

        # 保留删除的起始位置
        delStart = 0

        for index, char in enumerate(s):
            if char in dic:
                # 更新最大长度值
                if maxLen < tempLen:
                    maxLen = tempLen

                # 重置之前的部分记录
                # 注意，因为此时有重复的字母，所以，删除字典中该字符以及该字符之前的字符。
                # 因为，字典没有顺序，所以根据当前的字符，找到字典中存在的字符的下标，然后根据下标找到字符串中下标之前的所有字符，并删除它(们)
                # 并加入此时的字母，长度需要计算一下。
                delEnd = dic[char]
                # print(delEnd, char)
                # print(dic)

                for i in range(delStart, delEnd + 1):
                    dic.pop(s[i])
                    tempLen -= 1

                delStart = delEnd + 1

                # print(dic)
                # 将当前字符加入进入
                dic[char] = index
                tempLen += 1

                # print(dic)
                # break

            else:
                # 保留子串
                dic[char] = index
                tempLen += 1

        # 注意，最后结束的时候，也要判断一下，因为只有当出现重复的时候，才会判断。
        # 但是如果一个字符串没有出现重复字符，那么就不会判断，所以需要额外判断一下。
        if maxLen < tempLen:
            maxLen = tempLen

        return maxLen


if __name__ == '__main__':

    # strs = "abcabcbb"
    # strs = "bbbbbb"
    # strs = "pwwkew"
    # strs = ""
    # strs = " "
    strs = "dvdf"

    sol = Solution()

    maxLen = sol.lengthOfLongestSubstring(strs)

    print(maxLen)
