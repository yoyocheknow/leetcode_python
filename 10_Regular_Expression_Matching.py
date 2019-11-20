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


if __name__ == "__main__":
    r = Solution().isMatch('aac', 'a*c')
    print r
