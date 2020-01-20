# -*- coding:utf-8 -*-

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        if length <= 1:
            return 0

        water_sum, left = 0, 0
        for i in range(length):
            if left == 0:
                if height[i] == 0:
                    continue
                else:
                    left = height[i]
            # 右边是否有比左挡板大的值
            has_big_right = False
            t = i + 1
            second_big_right = 0
            while (t < length):
                if height[t] >= height[i]:
                    has_big_right = True
                    break
                else:
                    # 记录右边最大的一个值
                    second_big_right = height[t] if height[t] > second_big_right else second_big_right
                t += 1
            # 若右边有比左挡板还要大的值
            if has_big_right:

                if height[i] < left:
                    water_sum = water_sum + left - height[i]
                else:
                    left = height[i]
            else:
                # 若右边没有比hegight[i]还要大的值，那么现在左挡板值就为比hegight[i]次大的值
                left = second_big_right
        return water_sum

if __name__ == "__main__":
    r = Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])
    print r