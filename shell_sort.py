# -*- coding:utf-8 -*-


class Solution(object):
    # 希尔排序整体思想：任意间隔为h的数组是有序的。然后缩小这个间隔h
    def shellSort(self, l):
        h=1
        while h<len(l)/3:
            h=3*h+1
        while h>=1:
            for i in range(h,len(l)):
                for j in range(i,h,-h):
                    if l[j]<l[j-h]:
                        l[j],l[j-h]=l[j-h],[j]
                h=h/3


        return l

if __name__ == "__main__":
    r = Solution().shellSort([9,2,5,4,3,1,6,7,8])

    print r