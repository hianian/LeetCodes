"""
    思路2：
        在思路1中，当遇到重复元素时，就把字典中存在元素及其之前的元素都删掉，这样就可以很方便地
        判断之后的元素了。

        但是也可以不用这么做，只需要及时地更新“起始计算长度的位置”即可。

        计算长度的位置start，见下面的具体描述，需要特殊判断一下，防止start往回走。
"""


class Solution:
    def lengthOfLongestSubstring(self, s):

        dic = {}
        maxLen = 0
        start = 0
        for index in range(len(s)):
            if s[index] in dic:
                # 注意，因为没有弹出之前已经存在的元素，所以，如果当前元素在字典中已经存在，并且字典中的下标在当前start的前面，
                # 那么就说明当前元素之前已经存在了重复元素，比如 abba 这样的，当检测到b重复时，start就到了 下标2 的位置，
                # 但是如果检测到a时，start不应该回到 下标1 的位置。所以需要单独判断一下。
                if start < dic[s[index]] + 1:
                    start = dic[s[index]] + 1

            # 每次都判断最大长度是否需要更新
            if maxLen < index - start + 1:
                maxLen = index - start + 1

            dic[s[index]] = index

        return maxLen


if __name__ == '__main__':

    # strs = "abcabcbb"
    # strs = "bbbbbb"
    # strs = "pwwkew"
    # strs = ""
    # strs = " "
    strs = "abcde"
    # strs = "dvdf"
    # strs = "cdd"
    # strs = "abba"
    # strs = "nfpdmpi"

    sol = Solution()

    maxLen = sol.lengthOfLongestSubstring(strs)

    print(maxLen)

