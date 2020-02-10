# -*- coding:utf-8 -*-


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        max_sum=0
        for i in range(len(heights)):
            left=i
            right=i+1
            sum=0
            while(left>=0 and heights[left]>=heights[i]):
                sum+=heights[i]
                left-=1
            while(right<len(heights) and heights[right]>=heights[i]):
                sum+=heights[i]
                right+=1

            max_sum = sum if sum>max_sum else max_sum

        return max_sum

    # using stack - O(n)
    #整体思路是，遍历这个数组，每次遇见当前的数值小于前面的数值，就计算前面所围城的长方形的面积。
    #用一个栈来保存前面的数值，每当当前值小于前面的数值的话heights[index] < heights[stack[-1]]，就弹出最近的一个当前值，
    #并计算长方形面积。依次往前判断。
    def largestRectangleArea1(self,heights):
        stack, area = [-1], 0
        heights.append(-1)  # used to pop remaining entries, since heights in input are positive
        for index in range(len(heights)):
            while heights[index] < heights[stack[-1]]:
                curr_height = heights[stack.pop()]
                width = index - stack[-1] - 1  # right-left
                area = max(area, curr_height * width)
            stack.append(index)
        return area
if __name__ == "__main__":
    r = Solution().largestRectangleArea1([2,1,5,6,2,3])
    print r