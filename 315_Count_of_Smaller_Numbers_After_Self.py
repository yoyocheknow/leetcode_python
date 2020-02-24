# -*- coding:utf-8 -*-

class Solution(object):
    # 分治思想。假设有两个有序的数组，然后去求他们的逆序数，可以在归并的时候去求。
    # 具体操作是，比如数组[-7,1,5,9]和[-2,1,3,5] 归并前他们的逆序数分别为[0,1,3,4],[0,0,0,0]
    # 在归并的时候，比如-7<-2，那么-7对应的逆序数为0。然后比较1和-2，这个时候-2被排序，且逆序数为0，
    # 然后1 和 1比较，1<=1,那么左边的1对应的逆序数就应该是右边1 的下标值即1。因为左右两个序列都是升序的，
    # 那么比左边1小的数，只能是右边序列中比1小的数。所以应该是右边1 的下标。
    # 归并完以后，逆序数就求出来了。所以前期要先分割，然后排序，最后归并。
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums)<1:
            return []
        pair=[{nums[i]:i} for i in range(len(nums))]
        count=[0]*len(nums)


        self.merge_sort(pair,count)
        return count

    def merge_sort(self,pair,count):
        if len(pair) < 2:
            return pair
        mid = len(pair) / 2

        list1=self.merge_sort(pair[:mid],count)
        list2=self.merge_sort(pair[mid:],count)

        return self.merge_sort_two_list(list1, list2, count)

    def merge_sort_two_list(self, list1, list2, count):
        i, j = 0, 0
        res=[]
        while i < len(list1) and j < len(list2):
            if list1[i].keys()[0] <= list2[j].keys()[0]:
                count[list1[i].values()[0]] += j
                res.append(list1[i])
                i += 1
            else:
                res.append(list2[j])
                j += 1
        while i < len(list1):
            count[list1[i].values()[0]] += j
            res.append(list1[i])
            i += 1
        while j < len(list2):
            res.append(list2[j])
            j += 1
        return res

if __name__ == "__main__":
    r = Solution().countSmaller([-1])
    print r




