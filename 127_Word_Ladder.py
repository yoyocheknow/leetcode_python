# -*- coding:utf-8 -*-

from collections import defaultdict
import collections
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        # Since all words are of same length.
        L = len(beginWord)

        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        all_combo_dict = defaultdict(list)
        print all_combo_dict
        for word in wordList:
            for i in range(L):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                # key是中间匹配字符值：比如遍历完hit这个字符后，all_combo_dict存入的是：{'h*t':[hot],'*ot':[hot],'ho*':[hot]}
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)

        # Queue for BFS
        queue = collections.deque([(beginWord, 1)])
        # Visited to make sure we don't repeat processing same word.
        visited = {beginWord: True}
        while queue:
            current_word, level = queue.popleft()
            for i in range(L):
                # 计算当前值的中间变量比如hit，中间值为：*it,h*t,hi*
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]

                # Next states are all the words which share the same intermediate state.
                # all_combo_dict存的是中间值多对应的字符比如，'h*t':['hot'],'*ot':['hot','dot','lot']
                for word in all_combo_dict[intermediate_word]:
                    # If at any point if we find what we are looking for
                    # i.e. the end word - we can return with the answer.
                    # 如果找到了这个endword，则即为所得答案
                    if word == endWord:
                        return level + 1
                    # Otherwise, add it to the BFS Queue. Also mark it visited
                    # 如果这个word没有被访问过的话，标记这个word已经访问过，防止循环遍历
                    # 并把这个word作为中间值，记录下来，层数加1
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                all_combo_dict[intermediate_word] = []
        return 0

if __name__ == "__main__":

    r = Solution().ladderLength('hit','cog',["hot","dot","dog","lot","log","cog"])
    print r