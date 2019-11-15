# -*- coding:utf-8 -*-


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        res_list,i ,j=[], 0, 0
        len1 = len(nums1)
        len2 = len(nums2)
        length = len1+len2
        while(i<len1 and j < len2):
            if nums1[i] <nums2[j]:
                res_list.append(nums1[i])
                i+=1
            else:
                res_list.append(nums2[j])
                j+=1
        while(i<len1):
            res_list.append(nums1[i])
            i+=1
        while(j<len2):
            res_list.append(nums2[j])
            j += 1
        print res_list
        if length % 2 == 0:
            return (res_list[(length / 2)-1] + res_list[(length / 2)])/2.0
        else:
            return res_list[(length / 2)]/2.0


if __name__ == "__main__":
    r = Solution().findMedianSortedArrays([1,2,4],[3,5,6])
    print r