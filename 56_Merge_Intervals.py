# -*- coding:utf-8 -*-


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        res_lsit=[]

        if len(intervals)<=1:
            return intervals
        # 排序
        intervals.sort(key=lambda x: x[0])
        print intervals
        temp=intervals[0]
        res_lsit.append(temp)
        for i in range(1,len(intervals)):
            if temp[1]<intervals[i][0]:

                res_lsit.append(intervals[i])
                temp=intervals[i]
            else:

                left=temp[0] if temp[0]<intervals[i][0] else intervals[i][0]
                right = temp[1] if temp[1]>intervals[i][1] else intervals[i][1]
                temp=[left,right]
                if res_lsit[-1][0]>=temp[0]:
                        res_lsit[-1]=temp
                else:
                    res_lsit.append(temp)

        return res_lsit

if __name__ == "__main__":
    r = Solution().merge([[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]])
    print r
