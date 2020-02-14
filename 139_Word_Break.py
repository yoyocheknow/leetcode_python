# -*- coding:utf-8 -*-


class Solution(object):

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False for i in range(len(s) + 1)]
        dp[0] = True

        for i in range(len(s)):
            if dp[i]:
                for j in range(i, len(s)):
                    if s[i:j + 1] in wordDict:  # as in [i:j+1] it will take from i to j
                        dp[j + 1] = True  # as we made empty string as our zero position hence each increased by 1

        return dp[-1]

if __name__ == "__main__":
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    # s='ccbb'
    # wordDict=["bc","cb"]
    r = Solution().wordBreak(s,wordDict)
    print r