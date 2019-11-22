# -*- coding:utf-8 -*-


class Solution(object):
    # 借助2_sum的求和方法，竟然超时
    def threeSum1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res_list=[]

        for i in range(len(nums)):
            temp_list = []
            diff = 0-nums[i]
            h={}

            for j in range(len(nums)):
                if i ==j:
                    continue
                temp = nums[j]
                diffff = diff - temp
                if diffff not in h:
                    h[temp] = j
                else:
                    temp_list=[nums[i], diffff, nums[j]]
                    temp_list.sort()

                if temp_list and temp_list not in res_list:
                    res_list.append(temp_list)


        return res_list

    # 双指针法
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res_list=[]
        nums.sort()

        for i in range(len(nums)):
            if nums[i]>0:
                # 如果第一个元素就大于0，后面就不用遍历了，后面全部大于0
                break
            if i>0 and nums[i] == nums[i-1]:
                # 跳过重复元素
                continue
            left = i+1
            right = len(nums)-1
            while(left<right):
                sum = nums[i] +nums[left]+nums[right]
                if sum == 0:
                    temp_list = [nums[i], nums[left], nums[right]]
                    res_list.append(temp_list)
                    # 循环校验。由于数组已经有序，所以这个操作可以跳过那些重复元素
                    # 从而可以对结果去重
                    while(left<right and nums[left] ==temp_list[1]):
                        left +=1
                    while (left < right and nums[right] == temp_list[2]):
                        right -= 1
                elif sum>0:
                    right -=1
                else:
                    left +=1

        return res_list



if __name__ == "__main__":
    r = Solution().threeSum([-1, 0, 1, 2, -1, -4])
    print r


