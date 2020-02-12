# -*- coding:utf-8 -*-


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res_list=[]
        if numRows<1:
            return
        res_list.append([1])
        for i in range(1,numRows):
            now_floor=[]
            now_floor.append(1)
            for j in range(1,len(res_list[-1])):
                temp=res_list[-1][j]+res_list[-1][j-1]
                now_floor.append(temp)
            now_floor.append(1)
            res_list.append(now_floor)

        return res_list


if __name__ == "__main__":

    r=Solution().generate(5)

    print r