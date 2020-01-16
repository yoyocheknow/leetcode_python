# -*- coding:utf-8 -*-

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle=='':
            return 0
        for i in range(len(haystack)):
            if haystack[i]!=needle[0]:
                continue
            else:
                if haystack[i:i+len(needle)] == needle:
                    return i
                else:
                    continue
        return -1

if __name__ == "__main__":
    r = Solution().strStr('hello','oqq')
    print r