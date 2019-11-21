# -*- coding:utf-8 -*-


class Solution(object):
    # 常规解法，暴力，超时
    def maxArea1(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area=0
        for i in range(len(height)):
            for j in range(len(height)):
                h = height[i] if height[i] < height[j] else height[j]
                max_area = h * abs(j-i) if h * abs(j-i) > max_area else max_area
        return max_area

    # 双指针法
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area, i, j=0, 0 , len(height)-1
        while(i<j):
            max_area = max(max_area, min(height[i], height[j]) * (j-i))
            if height[i]<height[j]:
                # 向右移动i
                k = i + 1
                while(height[k]<=height[i] and k<j):
                    k += 1
                i = k
            else:
                # 向左移动j
                k=j-1
                while(height[k]<=height[j] and i <k):
                    k -= 1
                j=k
        return max_area

if __name__ == "__main__":
    r = Solution().maxArea([3,2,1,3])
    print r

