# -*- coding:utf-8 -*-


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        temp = None
        is_has_one=False
        for i in nums:
            if not temp and i >0:
                temp=i
            else:
                pass
            if i >0 :
                if i == 1:
                    is_has_one=True
                elif i==temp+1:
                    temp=i
                else:
                    continue
            else:
                continue
        return temp+1 if is_has_one else 1
    #更简单的思路
    def firstMissingPositive1(self, nums):
        nums.sort()
        temp = 1
        for i in nums:
            if i == temp:
                temp += 1
        return temp

if __name__ == "__main__":
    r = Solution().firstMissingPositive([7,8,9,11,12])
    print r
