# -*- coding:utf-8 -*-

class Solution(object):
    # 将正数与负数分开
    # 先将负数与非负数分开
    # 然后再把非负数中的正数与0分开
    def divser_number(self ,arr):
        l=0
        r=len ( arr)-1
        while l<r:
            if arr[l]<0:
                l+=1
            if arr[r]>=0:
                r-=1

            if arr[l]>=0 and arr[r]<0:
                arr[l],arr[r ]=arr[ r ],arr[l ]
                l+=1
                r-=1

        print arr
        l = 0
        r = len(arr) - 1
        while l < r:
            if arr[l] <= 0:
                l += 1

            if arr[r] > 0:
                r -= 1

            if arr[l] > 0 and arr[r] == 0:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
        return arr

if __name__ == "__main__":
    r = Solution().divser_number([-1,-4,3,2,0,2,-2,0])

    print r