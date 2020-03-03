# -*- coding:utf-8 -*-

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # 大致思路是，每次拿出一个点，跟其他点比较。用一个dict来记录斜率相同的数目。
        # 然后把某个斜率数目最大的值记录下来
        def helper(currentPoint, points):
            slopes, duplicates, ans = {}, 0, 0
            x1, y1 = currentPoint
            for x2, y2 in points:
                # If the points are same inc duplicate counter
                if x1 == x2 and y1 == y2:
                    duplicates += 1
                # else find the slop and add in dic
                else:
                    from fractions import Fraction
                    # 以分数的形式作为key存储而不是 小数
                    slope = Fraction(x2 - x1,y2 - y1) if y2 != y1 else 'inf'
                    count = slopes.get(slope, 0) + 1
                    slopes[slope] = count
                    ans = max(ans, count)
            return ans + 1 + duplicates

        ans = 0
        while points:
            currentPoint = points.pop()
            ans = max(ans, helper(currentPoint, points))
        return ans

if __name__ == "__main__":

    r = Solution().maxPoints([[-4,1],[-7,7],[-1,5],[9,-25]])

    print r


