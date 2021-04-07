"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
    思路3：
        参考其他解题的方法，采用字典的方式。（主要是依靠字典Hash的查找算法）
        Python中的字典，采用Hash表，所以查找是否某元素存在的时间复杂度是O(1)。
        
        上面的两种方法都是根据元素求和，来判断是否满足target。
        可以换种思路。用目标值减去元素值，看看结果是否在剩下的元素中。
            1) 目标值减去元素值，遍历每个元素，这个就需要遍历列表。
            2) 接下来就是判断结果值是否在其他的元素中找到。这个时候，可以用字典。将元素作为关键字key，将下标作为值value。
            
        一种方法就是先遍历一遍，将所有的数据全部存储在字典中；然后再次遍历，判断字典中是否存在结果值。
        （这样，就需要遍历两次；而且如果两个数是相同的情况下，还需要去重。还有一种情况，就是比如结果值和元素值一样的情况下，也需要去重）

        '''
        # 这种方法行不通，如果事先将全部元素存储到字典中，那么在判断的时候需要去重。
        # 比如目标值是6，有一个元素是3，那么在判断是否在字典中的时候，这个元素3会干扰字典的查找结果。
        # 或许可以在遍历字典，逐个取出元素。
        # 但是这种将数据提前存储到字典的方法，如果两个元素相同，那么在字典中就会覆盖掉原始数据。
        # 比如 [2, 2, 3, 6, 0]。那么两个元素2，就会覆盖掉一个。
        hashmap = {}

        for index, num in enumerate(nums):
            hashmap[num] = index

        for num in nums:
            result = target - num
            hashmap.pop(num)
            if result in hashmap:
                return nums.index(num), hashmap[result]
        '''        
        
        另一种方法就是，因为是需要找两个数，那么其实可以不用事先将它们存入字典中，逐个遍历的时候，顺带将其放入字典即可。
        （如果存在两个数的话，即使在判断第一个数的时候，没有在字典中找到；但是在判断第二个数的时候，一定会在字典中找到第一个数）
        （换句话说，如果存在两个数，那么在遍历完之后，一定能找到结果值）
        
        这样的话，基于字典，就可以很方便的查找到数据，只需要一次遍历，
        
        如果遍历完，仍然没有找到元素，则说明，列表中没有两个元素满足要求。
"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], index]
            hashmap[num] = index
        return None


if __name__ == '__main__':
    sol = Solution()
    # nums, target = [15, 4, 15, 4], 8
    # nums, target = [-1, -2, -3, -4, -5], -8
    # nums, target = [3, 2, 95, 4, -3], 92

    nums, target = [2, 2, 7, 11, 15], 4

    index_s, index_e = sol.twoSum(nums, target)

    print(index_s, index_e)
