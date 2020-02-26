
# -*- coding:utf-8 -*-
import collections
class Solution(object):
    coursesMap = None
    # 深度优先遍历。解决思路在于这个图是否有环。
    # white 代表还未开始遍历的点，gray代表正在遍历的点，black代表已经遍历过的点
    # dfs返回是否有环，有环为True
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        white = set()
        gray = set()
        black = set()
        self.coursesMap = collections.defaultdict(list)

        for i in range(numCourses):
            white.add(i)
        for edge in prerequisites:
            self.coursesMap[edge[1]].append(edge[0])

        for i in range(numCourses):
            if self.dfs(i, white, gray, black):
                return False
        return True

    def dfs(self, curr, white, gray, black):
        if curr in white:
            white.remove(curr)
        gray.add(curr)

        for neighbor in self.coursesMap[curr]:
            if neighbor in black:
                continue
            if neighbor in gray:
                return True
            if self.dfs(neighbor, white, gray, black):
                return True
        if curr in gray:
            gray.remove(curr)
        black.add(curr)

    def bfs(self, curr, white, gray, black):

        return False

if __name__ == "__main__":

    r = Solution().canFinish(3,[[0,1],[0,2],[1,2]])
    print r