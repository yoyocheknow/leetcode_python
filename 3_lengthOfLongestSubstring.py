# -*- coding:utf-8 -*-


class Solution(object):
    # 其实这道题我卡了很久，原因是不知道python从i+1的地方遍历，然后就想到用while的方式，每次for循环一次，就把上一次循环过的字符删掉
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        tmp_list=[]
        max_length=1
        length=len(s)
        s_copy=list(s)
        while(length>0):
            for i, v in enumerate(s_copy):
                if v not in tmp_list:
                    tmp_list.append(v)
                else:
                    max_length=len(tmp_list) if len(tmp_list)>max_length else max_length
                    tmp_list = []
                    s_copy.pop(0)
                    break
            length-=1
        return max_length
    # 上面那个算法是不知道如何i+1遍历，可以用range(),但是这个o(n^2)，会超时，但是和上一个其实是一个思路
    def lengthOfLongestSubstring1(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        tmp_list=[]
        max_length=1
        s_copy=list(s)
        for i in range(len(s_copy)):
            for j in range(i, len(s_copy)):
                if s_copy[j] not in tmp_list:
                    tmp_list.append(s_copy[j])
                else:
                    max_length = len(tmp_list) if len(tmp_list) > max_length else max_length
                    tmp_list = []
                    break

        return max_length

    #滑动窗口的思想解决
    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        """
        length, i, j, max_length = len(s), 0, 0, 0
        s_copy = list(s)
        slide_window=set()
        while(i<length and j <length):
            if s_copy[j] not in slide_window:
                slide_window.add(s_copy[j])
                j+=1
                max_length=max(max_length, j-i)
            else:
                slide_window.remove(s_copy[i])
                i+=1
        return max_length

if __name__ == "__main__":
    r = Solution().lengthOfLongestSubstring1('abaabcbb')
    print r