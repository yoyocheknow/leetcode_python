# -*- coding:utf-8 -*-

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res_list=[]
        def Expand(nums,index,target,left,right):
            i,j = index,index

            while(i>=left):
                if nums[i]==target:
                    i-=1
                else:
                    break
            while(j<=right):
                if nums[j]==target:
                    j+=1
                else:
                    break
            return i+1,j-1

        left =0
        right = len(nums)-1
        while(left<=right):
            mid = (left+right)/2
            if nums[mid]==target:
                i,j = Expand(nums,mid,target,left,right)
                res_list.append(i)
                res_list.append(j)
                break
            if target>=nums[mid]:
                left=mid+1
            else:
                right = mid-1
        if len(res_list)==0:
            res_list.append(-1)
            res_list.append(-1)
        return res_list


if __name__ == "__main__":
    r = Solution().searchRange([5,7,7,8,8,8,8,10],10)
    print r