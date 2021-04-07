"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
    思路2：
        参考其他解题的方法：首位递进查找
        对元素进行排序（升序），首尾元素相加，
        如果两数之和大于目标值，那么就需要减小元素的值，因为已经排好序了，所以只能从末尾倒序选择元素。
        如果两数之和小于目标值，那么就需要增加元素的值，因为已经排好序了，所以只能从开头正序选择元素。
        
        而因为题目中指明了，只有一个结果，所以找到后直接返回即可。
        
        但是提交的时候，执行时间相比方法1反而变长了。
"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # 根据元素的大小，对下标索引进行排序。(注意，题目要求的是返回元素的下标)
        # 比如 [3, 2, 95, 4, -3], 根据元素大小对下标索引进行排序(从小到大)。
        # 最小的值是-3，它的下标是4, 其次是2, 下标是1；所以排序后的下标值 [4, 1, 0, 3, 2]
        # sorted函数就是：对第一个参数进行排序，key就是根据什么来对第一个参数进行排序
        # （就是将第一个参数的各个元素输入到key中，根据输出进行排序），默认是升序。
        sortedIndex = sorted(range(len(nums)), key=lambda x: nums[x])
        head = 0
        tail = len(nums) - 1
        tempTarget = nums[sortedIndex[head]] + nums[sortedIndex[tail]]

        while tempTarget != target:
            if tempTarget < target:
                head += 1
            else:
                tail -= 1
            tempTarget = nums[sortedIndex[head]] + nums[sortedIndex[tail]]

        return sortedIndex[head], sortedIndex[tail]


if __name__ == '__main__':
    sol = Solution()
    # nums, target = [15, 4, 15, 4], 8
    # nums, target = [-1, -2, -3, -4, -5], -8
    # nums, target = [3, 2, 95, 4, -3], 92

    nums, target = [2, 2, 7, 11, 15], 4

    index_s, index_e = sol.twoSum(nums, target)

    print(index_s, index_e)
