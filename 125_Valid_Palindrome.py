# -*- coding:utf-8 -*-
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l=[]
        for str in s:
            if ord(str)>=65 and ord(str)<=90:
                l.append(str)
            if ord(str)>=97 and ord(str)<=122:
                l.append(str)
            if ord(str)>=48 and ord(str)<=57:
                l.append(str)
        print l
        for i in range(len(l)):
            if l[i].lower()!=l[len(l)-1-i].lower():
                return False
        return True

if __name__ == "__main__":

    r = Solution().isPalindrome('0p')
    print r