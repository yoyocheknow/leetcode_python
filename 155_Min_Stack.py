# -*- coding:utf-8 -*-
import sys

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[float('inf')]
        self.min_stack=[float('inf')]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        self.min_stack.append(min(x,self.min_stack[-1]))

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()

        self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]

if __name__ == "__main__":
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    obj.push(4)
    obj.push(-5)
    print obj.min_stack
    print obj.stack
    print obj.getMin()
    obj.pop()

    print obj.top()
    print obj.getMin()
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()