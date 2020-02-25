# -*- coding:utf-8 -*-


class Solution(object):
    # 贪心算法解这道题。
    # 每当一个数字比前一个数字更大或者更小的时候，此时这个序列正处于上升或者下降的趋势，
    # 那么我们应该取这个趋势中上升的最大，或者下降的最小的那个数字，因为只有这样，后面才能更容易的成为一个摇摆序列。
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2:
            return len(nums)
        res=[]
        res.append(nums[0])
        length=1
        state='BEGIN'
        for i in range(1,len(nums)):
            dif = nums[i] - nums[i - 1]
            if state=='BEGIN':
                if dif>0:
                    state='UP'
                    length+=1
                elif dif<0:
                    state='DOWN'
                    length+=1
                continue
            if state == 'UP':
                if dif < 0:
                    state = 'DOWN'
                    length += 1
                continue
            if state=='DOWN':
                if dif>0:
                    state='UP'
                    length+=1
                continue

        return length

if __name__ == "__main__":
    r = Solution().wiggleMaxLength([1,17,5,10,13,15,10,5,16,8])
    print r