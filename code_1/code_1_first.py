"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
思路1：
    多次遍历：
        外层循环，遍历元素并记录index_start，然后从该元素的下一个位置继续遍历，直到找到那个值index_end或者到达列表结尾
        如果到达结尾仍然没有找到，则再次循环，将本次记录的元素的下一个元素index_start.
    
    注意，不能简单的寻找比目标值小的元素作为初步筛选的条件，因为一个元素是正数，一个元素是负数，最终的目标值可能比正数小。

    所以只能暴力遍历，遍历各个元素。
"""

class Solution:
    def twoSum(self, nums, target):

        # 数组中有重复的数字，所以不能用字典，值作为关键字key，下标index作为值value。
        # candidate_index = []
        index_s = 0

        for num in nums:

            # 注意，还要考虑负数的情况。负数相加越来越小。
            # 正数和负数相加，以及负数和正数相加，都有可能出现结果。所以应该判断某个元素和目标值的相对大小来进行筛选
            # if num <= target or abs(num) <= abs(target):
                # candidate
                # candidate_index.append(index_s)

            index_e = index_s + 1
            for sub_num in nums[index_s + 1:]:
                if num + sub_num == target:
                    return index_s, index_e

                index_e += 1

            index_s += 1


if __name__ == '__main__':
    sol = Solution()
    # nums, target = [15, 4, 15, 4], 8
    # nums, target = [-1, -2, -3, -4, -5], -8
    # nums, target = [3, 2, 95, 4, -3], 92

    nums, target = [2, 2, 7, 11, 15], 4

    index_s, index_e = sol.twoSum(nums, target)

    print(index_s, index_e)
