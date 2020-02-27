# -*- coding:utf-8 -*-

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        output=[]
        candidates.sort()
        def backtrack(i,sum,item):
            if i>=len(candidates) or sum>target:
                return
            item.append(candidates[i])
            sum +=candidates[i]
            if sum==target and item not in output:
                output.append(item)
            backtrack(i+1,sum,item[:])
            sum-=candidates[i]
            backtrack(i + 1, sum, item[:-1])
        backtrack(0,0,[])
        return output

if __name__ == "__main__":
    r = Solution().combinationSum2( [10,1,2,7,6,1,5],8)
    print r
