# -*- coding:utf-8 -*-


class Solution(object):
    #常规法，遍历所有的子字串，然后判断子字串是否是回文，返回最长的那一个
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res_list = ''
        for i in range(len(s)):
            temp_list = ''
            for j in range(i, len(s)):
                temp_list += s[j]
                if self.is_Palindrome(temp_list):
                    res_list = res_list if len(temp_list)<len(res_list) else temp_list
        return res_list

    def is_Palindrome(self,s):
        length = len(s)
        mid = length / 2
        if length == 2:
            if s[0]==s[1]:
                return True
            else:
                return False
        for i in range(0, mid):
            if s[i] != s[length - 1 - i]:
                return False
        return True

    # 从某个元素中心向两边遍历，如果相等则是回文。
    max_length = 0
    temp_str = ''
    def longestPalindrome1(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) ==1:
            return s

        for i in range(0,len(s)):
            self.checkPalindromeExpand(s, i, i)
            self.checkPalindromeExpand(s, i, i+1)
        return self.temp_str

    def checkPalindromeExpand(self,s,low,high):
        while(low>=0 and high <len(s)):
            if s[low]==s[high]:
                if high - low + 1 > self.max_length:
                    self.max_length = high - low + 1
                    self.temp_str = s[low:high+1]
                low -= 1
                high += 1

            else:
                return


if __name__ == "__main__":
    r = Solution().longestPalindrome1('aba')
    print r