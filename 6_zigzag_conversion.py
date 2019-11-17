# -*- coding:utf-8 -*-


class Solution(object):
    #用一个字符串数组 ans[rows] 来存储每一行，最后一拼接就是最终结果。
    #用一个delta表示正向还是反向，即上图中从第一行到最后一行还是最后一行到第一行

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s)==0 or numRows <=1:
            return s
        ans=['' for _ in range(numRows)]
        row, delta =0, 1
        for i in range(0, len(s)):
            ans[row] += s[i]
            row += delta
            #说明此时该折回换行了
            if(row >=numRows):
                row = numRows-2
                delta=-1
            #折到头以后重新开始
            if row <0:
                row =1
                delta=1
        res=''
        for v in ans:
            res+=v
        return res

if __name__ == "__main__":
    r = Solution().convert('PAYPALISHIRING', 3)
    print r