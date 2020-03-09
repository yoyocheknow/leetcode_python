# -*- coding:utf-8 -*-


class Solution(object):
    # 插入排序整体思想：将一个元素插入到前面已经有序数组的合适位置
    def insertSort(self, l):

        for i in range(1,len(l)):
           for j in range(i,0,-1):
               if l[j]<l[j-1]:
                   l[j],l[j-1]=l[j-1],l[j]

        return l

if __name__ == "__main__":
    r = Solution().insertSort([9,2,5,4,3,1,6,7,8])

    print r