# -*- coding:utf-8 -*-


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums=[i for i in range(1,n+1)]
        res=[]
        def backtrack(nums,arr1):
            if len(nums)==0:
                res.append(arr1)
            for i in range(len(nums)):
                cur=str(nums[i])
                others=nums[:i]+nums[i+1:]
                backtrack(others,arr1+cur)

        backtrack(nums,'')
        return res[k-1]
    # 这道题是求一个排序组合的第k个项，一开始我用了上面的方法，用回溯的方法求出所有的排列组合，然后找到第k个，但是会超时。
    # 下面方法的解题思路是这样的：首先我们看123，求第3个这个例子。123的排列组合如下：
    # 123   ｜求第三个项，答案明显是213。从所有的组合中查找规律，所有项的第一个数字1，2，3分别排在横线分割的三个区域中。
    # 132   ｜那么第k项的首字符应该是哪个？从这个例子可以看到是2，因为K=3，第三个落在了第二个区域。同时发现，每一个区域的个数是有规律的。
    # ---   ｜即=(n-1)!个。3个数字的话，每个区域是2个。4个数字的话给个区域是（4-1)!=6个，所以查找第k个项的首数字，就看k落在了哪一个区域
    # 213   ｜那么区域index=1,这个index也是原数组的第index数字。所以123排列组合的第3项的第一个数字为2。
    # 231   ｜接下来求第二个数字，这个时候缩小范围，只在第二个区域查找，并且数字变为了1，3两个。可以求出这时候第二个区域的k应该是k=k-div
    # ---   ｜k现在变成了1，表示在第二个区域的第1个位置，第二个区域的数字只剩1，3。所以第二个数字应该是index=0，即1，每次这么递归求就行了。
    # 312
    # 321
    def getPermutation2(self, n, k):
        def fact(n):
            r = 1
            for i in range(2, n + 1):
                r *= i
            return r

        nums = [str(i) for i in range(1, n + 1)]
        s = ''

        while (nums):
            div = fact(len(nums) - 1)
            idx = 0
            while (k > div):
                idx += 1
                k -= div
            s += nums.pop(idx)

        return s
if __name__ == "__main__":
    r = Solution().getPermutation2(2,2)

    print r