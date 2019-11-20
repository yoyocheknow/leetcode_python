# -*- coding:utf-8 -*-
'''
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
'''


class Solution(object):

    # 递归法
    def isMatch(self, text, pattern):
        # 首先判断pattern是否为空，这个是递归的终止条件，如果pattern为空，并且text也为空
        # 说明已经挨个匹配完了，直接返回true即可
        if not pattern:
            return not text
        # 如果text和pattern只剩下一个字符 那么判断这两个字符是否相等或者 pattern的这个字符是否为'.'即可
        # 两者只有一个字符是 递归方法的最基础的子问题
        first_match = bool(text) and pattern[0] in {text[0], '.'}

        # 如果pattern有超过两个以上的字符，则要递归的进行判断
        # 超过两个以上的字符需要分两种情况，带'*'和不带'*'
        # 不带'*'的话简单，就是下面else的操作，判断第一个字符是否匹配，然后剩下的字符 递归进行匹配
        # 带'*'的话，分两种情况，看这个* 的作用是什么：
        # 1，重复前面的字符，2，取消前面的字符也就是'*' Matches zero of the preceding element
        # 因为这两个都有可能使pattern匹配上text。所以 用了or来判断。
        # 这两个情况对应的操作分别是：
        # 1，first_match and self.isMatch(text[1:], pattern) 要是重复前面的字符，那么就要判断前面的字符是否匹配
        # 所以要有first_match的判断，然后取text第二个字符以后的串和pattern比较（这里有一个疑问那就是，text比较完第一个字符了，并且进入递归
        # 方法时向后移动了一位，但是pattern并没有移动指针）
        # 2，self.isMatch(text, pattern[2:]
        # 如果是取消pattern的前面一个字符，那么pateter前一个字符加字符'*'，都没有用了，都被消掉了，所以进入下一次递归时，text
        # 指针不需要移动，pattern的从后面两个开始移动取pattern[2:]
        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])

        # 解释下上面的那个疑问：为什么pattern中的*选择重复前面的字符时，在进入下一次递归方法时，pattern没有向后移动指针，而text向后移动了一位
        # 比如这个case：text='aac',pattern='a*c',在比较到第二个字符时，如果* 选择复制前面的字符a，那么进入下一次递归时，text='ac',
        # pattern='a*c'，这个时候又要作出判断，*选择复制前一个，还是连同前一个字符一起消失，这个时候first_match肯定为true，那么如果*还是选择复制
        # 下一个递归进入时就是：text='c',pattern='a*c',这个时候又要作出选择，*选择复制还是选择消失，此时如果进入or的这一个判断，选择消失，那么
        # 进入下个递归时：text='c',pattern='c',matched!

    # DP动态规划解法
    def isMatch1(self, text, pattern):
        # 用dp(i,j)来表示text[i:],pattern[j:] matched, text从第i+1个字符开始和pattern的第j+1个字符开始匹配
        # dp思想就是把问题分而治之，把大的问题拆成小问题解决。对于这个题，要想比较整个串是否匹配，那么就可以拆解成：
        # A:判断text[0]和 pattern[0]是否匹配以及 B:text[1:]和 pattern[1:]是否匹配这两个子问题解决。我们知道A问题很容易判断，
        # 只需要这样判断即可： first_match = i < len(text) and pattern[j] in {text[i], '.'}
        # B问题 还可以继续拆解为 B_A:text[1]和pattern[1]比较,B_B:text[2:]和pattern[2:]比较。这个就是dp的整体思路。
        # 如果没有 * 这个限制条件的话，那么就可以这么写：ans = first_match and dp(i + 1, j + 1)。然后将这个结果存在memo中
        # 现在有* 这个条件限制：'*' Matches zero or more of the preceding element. *要么和前一个字符一起消失，要么就复制前一个字符
        # 那么我们在计算 B问题（求剩余字串是否匹配）时把这个限制加上即可。
        # '*' 如果复制前一个字符，那么只需要判断前一个字符是否匹配，即first_match 为true，只有前一个字符匹配了，才有分解下一部分字串的必要
        # 也就是first_match and dp(i + 1, j)
        # '*' 如果是和前一个字符一起消失，那么pattern的指针j只需要往后移动两个即可，text不需要动，即：ans = dp(i, j + 2)



        # memo{}用来缓存这个结果
        memo = {}
        def dp(i, j):
            # 如果i,j 已经在memo中，则直接返回这个结果
            if (i, j) not in memo:
                # 如果j已经走到了pattern尽头，那么判断i是不是也走到尽头，如果不是，则ans为false不匹配，如果是则匹配
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}

                    if j + 1 < len(pattern) and pattern[j + 1] == '*':
                        # pattern剩余的字符中第二个为*，走下面的逻辑
                        ans = dp(i, j + 2) or first_match and dp(i + 1, j)
                    else:
                        # pattern剩余的字符中没有*，走下面的逻辑
                        ans = first_match and dp(i + 1, j + 1)
                #将结果缓存在memo中
                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)

if __name__ == "__main__":
    r = Solution().isMatch1('aac', 'a*c')
    print r
