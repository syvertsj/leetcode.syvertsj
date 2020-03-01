#!/usr/bin/env python

class Solution(object):

    pstack = []
    longestStr = ""
    
    def reset(self):
        self.pstack = []; self.longestStr = ""

    def findGreatestRange(self, parenStr):
    
        maxdiff = 0; index1 = 0; index2 = 0
        
        if len(self.pstack) == 0:
            index1 = 0; index2 = len(parenStr) - 1
            
        elif len(self.pstack) == 1:
            print "comparing %s and %s" % (0, self.pstack[0])
            if self.pstack[0] > maxdiff:
                index1 = 0; index2 = self.pstack[0]; maxdiff = self.pstack[0]
                
            print "comparing %s and %s" % (self.pstack[0], len(parenStr) - 1)
            if len(parenStr) - self.pstack[0] > maxdiff:
                index1 = self.pstack[0] + 1; index2 = len(parenStr); maxdiff = len(self.pstack) - self.pstack[0]
        else:
            for i in range(len(self.pstack) - 1):
                print "comparing %s and %s" % (self.pstack[i], self.pstack[i+1])
                if self.pstack[i+1] - self.pstack[i] > maxdiff:
                    index1 = self.pstack[i] + 1; index2 = self.pstack[i+1]; maxdiff = self.pstack[i+1] - self.pstack[i]
        
        return (index1, index2)

    def findLongestString(self, parenStr):
        
        if len(self.pstack) == 0: 
            self.longestStr = parenStr
        else: 
            (start, end) = self.findGreatestRange(parenStr)
            self.longestStr = parenStr[start:end] if len(parenStr[start:end]) > 0 else ""
            
        return self.longestStr
    
    def findLongestValidParentheses(self, parenStr):
        
        for (i, p) in enumerate(parenStr):
            if p == "(": 
                self.pstack.append(i)
            else: 
                if len(self.pstack) > 0: self.pstack.pop()
                else: self.pstack.append(i)
            
            print self.pstack
        
        return self.findLongestString(parenStr)
    
    def longestValidParentheses(self, parenStr):
        
        self.reset()
        
        returnStr = self.findLongestValidParentheses(parenStr)
        explanation = "The longest valid parentheses substring is %s" % returnStr
        
        return (parenStr, len(returnStr), explanation)

if __name__ == "__main__":
    solution = Solution()
    print "Input: %s \nOutput: %s \nExplanation: %s \n" % (solution.longestValidParentheses( "()" ))
    print "Input: %s \nOutput: %s \nExplanation: %s \n" % (solution.longestValidParentheses( ")(" ))
    print "Input: %s \nOutput: %s \nExplanation: %s \n" % (solution.longestValidParentheses( "(()" ))
    print "Input: %s \nOutput: %s \nExplanation: %s \n" % (solution.longestValidParentheses( "(())" ))
    print "Input: %s \nOutput: %s \nExplanation: %s \n" % (solution.longestValidParentheses( "()(())(" ))
    print "Input: %s \nOutput: %s \nExplanation: %s \n" % (solution.longestValidParentheses( "()(()))" ))
