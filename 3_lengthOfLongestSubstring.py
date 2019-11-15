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

if __name__ == "__main__":
    r = Solution().lengthOfLongestSubstring('')
    print r