# -*- coding:utf-8 -*-


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        dic = {1:'I',
               4:'IV',
               5:'V',
               9: 'IX',
               10:'X',
               40:'XL',
               50:'L',
               90:'XC',
               100:'C',
               400:'CD',
               500:'D',
               900:'CM',
               1000:'M'}
        res=''
        num_list = []
        mi = 0
        divisor = 10
        while(num>0):


            temp = num % divisor
            num = num - temp
            mi += 1
            divisor = divisor * 10
            num_list.append(temp)
        num_list.reverse()
        qian, bai, shi, ge='', '', '', ''
        for i in range(len(num_list)):
            if not dic.get(num_list[i]):
                qian_n =num_list[i] / 1000
                bai_n = num_list[i] /100
                shi_n = num_list[i]/10
                if qian_n >0:
                    qian += 'M' * qian_n
                    res += qian
                    continue
                elif bai_n >0:
                    if num_list[i] - 500>0:
                        num_list[i] = num_list[i] - 500
                        res += dic.get(500)
                    bai_n=num_list[i] /100
                    bai += 'C' * bai_n
                    res += bai
                    continue
                elif shi_n >0:
                    if num_list[i] - 50>0:
                        num_list[i] = num_list[i]-50
                        res+=dic.get(50)
                    shi_n = num_list[i] /10
                    shi += 'X' * shi_n
                    res += shi
                    continue
                else:
                    if num_list[i]-5>0:
                        num_list[i]=num_list[i]-5
                        res+=dic.get(5)

                    ge += 'I' * num_list[i]

                    res += ge
                    continue
            else:
                res+=dic.get(num_list[i])

        return res

if __name__ == "__main__":
    r = Solution().intToRoman(9)
    print r