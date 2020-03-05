# -*- coding:utf-8 -*-


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        def backtrack(item,target):
            if target ==0:
                res.append(item)
                return
            if target<0:
                return
            for i in range(len(candidates)):
                item.append(candidates[i])
                target-=candidates[i]
                backtrack(item[:],target)
                item.pop()
                target+=candidates[i]

        backtrack([],target)
        res_set=[]
        #对 结果去重
        for r in res:
            r.sort()
            if r not in res_set:
                res_set.append(r)
        return res_set

if __name__ == "__main__":
    candidates = [2, 3, 5]
    target = 8
    r = Solution().combinationSum(candidates,target)

    print r