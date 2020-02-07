class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num=0
        mi =1
        digits.reverse()
        for i in digits:
            num=num+i*mi
            mi=mi*10
        print num
        res = num+1
        res_list=[]
        while(res>=1):
            n=res%10
            res_list.append(n)
            res=(res-n)/10

        res_list.reverse()
        return res_list


if __name__ == "__main__":
    r = Solution().plusOne([4,3,2,1])
    print r