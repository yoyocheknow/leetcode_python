# -*- coding:utf-8 -*-

from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashMap = defaultdict(list)
        for word in strs:
            key = list(word)
            key.sort()
            hashMap[str(key)].append(word)

        results = []
        for key in hashMap.keys():
            results.append(hashMap[key])

        return results

if __name__ == "__main__":
    r = Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat","aet"])
    print r

