# -*- coding:utf-8 -*-


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        length = len(s)
        for i in range(len(s)):
            if s[i] != s[length - i -1]:
                return False
        return True


if __name__ == "__main__":
    r = Solution().isPalindrome(10)
    print r