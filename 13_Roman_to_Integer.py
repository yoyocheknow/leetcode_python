# -*- coding:utf-8 -*-


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {'I': 1,
               'IV': 4,
               'V': 5,
               'IX': 9,
               'X': 10,
               'XL': 40,
               'L': 50,
               'XC': 90,
               'C': 100,
               'CD': 400,
               'D': 500,
               'CM': 900,
               'M': 1000}
        temp_list, res, i =[], 0, 0

        while(i<len(s)):
            if i+1 <len(s) and dic.get(s[i]+s[i+1]):
                temp_list.append(dic.get(s[i]+s[i+1]))
                i +=2
            elif dic.get(s[i]):
                temp_list.append(dic.get(s[i]))
                i+=1
        print temp_list
        for j in temp_list:
            res += j
        return res

if __name__ == "__main__":
    r = Solution().romanToInt("IV")
    print r