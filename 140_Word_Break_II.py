# -*- coding:utf-8 -*-


class Solution(object):
    # DFS 方法竟然超时
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        res=[]
        def backtrack(s,break_word,wordDict):
            if s=='':
                # 把最后的空格去掉
                res.append(break_word[:-1])
                return
            for i in range(1,len(s)+1):
                if s[:i] in wordDict:
                    backtrack(s[i:],break_word+s[:i]+' ', wordDict)

        backtrack(s,'',wordDict)
        return res
    # 对上面的方法进行一下优化
    # 具体思路：从s的首字母挨个往后遍历，如果发现有从start到n的字符在 wordDict中，那么就再递归地把从n+1到len(s)的字符依次往后调用。
    # 递归的终止条件是：1，如果s到头了，那么返回空的二维数组
    #                2，如果以start开头的剩余部分已经在缓存memo里了，那么直接返回
    # 对于 helper返回的二维数组做如下处理：将已经匹配的s[start:i+1] 和返回的二维数组中的一维拼接，存到res中
    # 然后更新memo缓存的key为start的value。
    # 如果匹配，最后的start肯定为0，而且value也不为空
    def wordBreak2(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        memo={}
        def helper(s,start,n ,dict_set):
            if start==n:
                return [[]]
            if start in memo:
                return memo[start]
            res=[]
            for i in range(start ,n):
                if s[start:i+1] in dict_set:
                    for part in helper(s,i+1,n,dict_set):
                        res.append([s[start:i+1]]+part)
            memo[start]=res
            return res

        res=helper(s, 0, len(s), set(wordDict))

        return [" ".join(i) for i in res]

if __name__ == "__main__":
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    # s='ccbb'
    # wordDict=["bc","cb"]
    r = Solution().wordBreak2(s,wordDict)
    print r