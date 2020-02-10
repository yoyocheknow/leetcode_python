# -*- coding:utf-8 -*-


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        nums1[m:m+n]=nums2[:]
        for i in range(m+n):
            for j in range(i+1,m+n):
                if nums1[j]<nums1[i]:
                    nums1[j],nums1[i]=nums1[i],nums1[j]
        return nums1

if __name__ == "__main__":
    nums1 = [4,5,6,0,0,0]
    nums2 = [1,2,3]
    r = Solution().merge(nums1,3,nums2,3)
    print r

