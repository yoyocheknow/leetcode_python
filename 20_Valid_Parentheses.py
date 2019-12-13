# -*- coding:utf-8 -*-


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        brackets_dicts={
            '(':')',
            '{':'}',
            '[':']'
        }
        for str in s:
            if brackets_dicts.get(str):
                stack.append(str)
            else:
                if len(stack)==0:
                    return False
                elif brackets_dicts.get(stack[-1])==str:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False

if __name__ == "__main__":
    r = Solution().isValid('()[]{}')
    print r