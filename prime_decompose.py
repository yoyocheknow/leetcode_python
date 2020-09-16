# -*- coding:utf-8 -*-

class Solution(object):

    def prime_decompose(self, num,res):

        if num ==1:
            return [1]
        if self.is_prime(num):
            res.append(num)
            return
        else:
            # 分解成两个值
            deco_1 =2
            deco_2 = num/deco_1
            # 如果num可以被两个值分解，比如90可以被2和45分解，但是 45不能被2 和22分解
            while deco_1 *deco_2!=num:
                deco_1+=1
                deco_2 = num/deco_1
            self.prime_decompose(deco_1, res)
            self.prime_decompose(deco_2, res)
        return res


    def is_prime(self,num):
        if num==1:
            return False
        begin =2
        while begin<num:
            if num%begin==0:
                return False
            else:
                begin +=1

        return True


if __name__ == "__main__":
    r = Solution().prime_decompose(90,[])

    print r