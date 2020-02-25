# -*- coding:utf-8 -*-


class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
        points.sort()
        shoot=1
        shoot_begin=points[0][0]
        shoot_end=points[0][1]
        for i in range(1,len(points)):
            if points[i][0]<=shoot_end:
                shoot_begin = points[i][0]
                if shoot_end >points[i][1]:

                    shoot_end = points[i][1]
            else:
                shoot+=1
                shoot_begin = points[i][0]
                shoot_end = points[i][1]

        return shoot

if __name__ == "__main__":
    r = Solution().findMinArrowShots([[10,16], [2,8], [1,6], [7,12]])
    print r