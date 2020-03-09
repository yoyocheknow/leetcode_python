# -*- coding:utf-8 -*-


class Solution(object):
    # 选择排序整体思想：每次选出最小的，放在最前面
    # 先找出最小的放到第0个位置，再找出次小的放在第1个位置，以此类推。
    def selectSort(self, l):

        for i in range(len(l)):
            min_index=i
            for j in range(i+1,len(l)):
                if l[j]<l[min_index]:
                    # 记录最小值的index
                    min_index=j
            # 把i和后面中最小值交换
            l[i],l[min_index]=l[min_index],l[i]

        return l

if __name__ == "__main__":
    r = Solution().selectSort([9,2,5,4,3,1,6,7,8])

    print r