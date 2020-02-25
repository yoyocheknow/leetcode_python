# -*- coding:utf-8 -*-


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 贪心算法
        # 和55题不同的是，这个需要求最小跳跃的次数。所以不能在max_index处跳跃
        # 那么何时跳跃才能符合题意呢？当index>current_max_index 时，说明就该跳了.
        # 这个时候次数加1，它是在何处跳的？所以还要维护一个pre_max_index，是在pre_max_index所在的index跳的
        # 然后更新此时的current_max_index=pre_max_index，因为是在pre_max_index 跳的

        if len(nums)<2:
            return 0
        current_max_index=nums[0]
        pre_max_index=nums[0]
        jump_min=1
        for i in range(1,len(nums)):
            if i >current_max_index:
                jump_min+=1
                current_max_index = pre_max_index
            # 更新pre_max_index
            pre_max_index = max(pre_max_index, nums[i]+i)


        return jump_min

if __name__ == "__main__":
    r = Solution().jump([2,3,1,1,4])
    print r