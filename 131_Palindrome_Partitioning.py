# -*- coding:utf-8 -*-


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        solutions = []

        def backtrack(lis, s, k, n):
            if k == n:
                solutions.append(lis)
                return
            for x in range(k + 1, n + 1):
                word = s[k:x]
                if word[::-1] == word:
                    newlist = list(lis)
                    newlist.append(word)
                    backtrack(newlist, s, x, n)

        backtrack([], s, 0, len(s))
        return solutions

if __name__ == "__main__":

    r = Solution().partition('aab')
    print r
