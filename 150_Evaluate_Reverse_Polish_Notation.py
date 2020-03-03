# -*- coding:utf-8 -*-

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack=[]
        while(tokens):
            t=tokens.pop(0)
            if t=='+':
                operator1=stack.pop()
                operator2=stack.pop()
                res=operator1+operator2
                stack.append(res)
            elif t=='-':
                operator1 = stack.pop()
                operator2 = stack.pop()
                res = operator2 - operator1
                stack.append(res)
            elif t=='*':
                operator1 = stack.pop()
                operator2 = stack.pop()
                res = operator1 * operator2
                stack.append(res)
            elif t=='/':
                operator1 = stack.pop()
                operator2 = stack.pop()
                res = operator2 // operator1 if operator2 * operator1 > 0 else (operator2 + (-operator2 % operator1)) // operator1

                stack.append(res)
            else:
                stack.append(int(t))

        return stack[0]

if __name__ == "__main__":

    r = Solution().evalRPN(["4","3","-"])

    print r