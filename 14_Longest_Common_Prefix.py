# -*- coding:utf-8 -*-


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) ==0:
            return ''

        min_length, i = len(strs[0]), 0
        for v in strs:
            min_length = min(len(v), min_length)

        prefix =''

        while(min_length>0):

            for i in range(len(strs)):
                prefix = strs[0][:min_length]
                if prefix != strs[i][:min_length]:
                    min_length -= 1
                    prefix=''
                    break
                else:
                    if i == len(strs)-1:
                        prefix = strs[i][:min_length]
                        min_length=0

        return prefix

if __name__ == "__main__":
    r = Solution().longestCommonPrefix(["c","acc","ccc"])
    print r