# -*- coding:utf-8 -*-

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        g=len(gas)
        i=0
        res=[]
        j=0
        tank=0
        consume=0
        while(j/g<1):
            if len(res)==g:
                break
            if tank-consume+gas[j]<cost[j]:
                #中间有一个点到达不了，则清空结果集合
                res=[]
                consume=0
                tank=0
                j=(j+1)%g
                i+=1
                if i==g:
                    break
            else:
                #记录起点
                res.append(j)
                tank=tank-consume+gas[j]
                consume = cost[j]
                j = (j+1) % g

        print res
        if not res :
            return -1
        else:
            return res[0]

if __name__ == "__main__":
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    # gas = [4]
    # cost = [5]

    r = Solution().canCompleteCircuit(gas,cost)
    print r