class Solution(object):
    
    def findGreatestRange(self, pstack):
    
        maxdiff = 0; i1 = 0; i2 = 0
            
        for i in range(len(pstack) - 1):
            
            if pstack[i][1] == '': i1 =  pstack[i][0] 
            else:                  i1 =  pstack[i][0] + 1
                
            if pstack[i+1][1] == '': i2 =  pstack[i+1][0] + 1
            else:                    i2 =  pstack[i+1][0]
              
            if i2 - i1 > maxdiff: maxdiff = i2 - i1
        
        return maxdiff
        
    def longestValidParentheses(self, s):
        
        if s == "": return 0
        
        # stack of tuples containing indices and parentheses
        # invalid entries are non-empty, and empty values used to mark valid ranges, 
        pstack = []
        
        pstack.append((0, ''))  # put starting index in stack
        
        for (i, p) in enumerate(s):
            if p == "(": 
                pstack.append((i,'('))
            elif p == ")": 
                if len(pstack) > 0 and pstack[len(pstack)-1][1] == '(': 
                    pstack.pop()
                else: 
                    pstack.append((i,')'))
                       
        pstack.append((len(s) - 1, ''))  # put end index to stack

        return self.findGreatestRange(pstack)

if __name__ == "__main__":
    solution = Solution()
    print solution.longestValidParentheses( "()" )
    print solution.longestValidParentheses( ")(" )
    print solution.longestValidParentheses( "(()" )
    print solution.longestValidParentheses( "(())" )
    print solution.longestValidParentheses( "()(())(" )
    print solution.longestValidParentheses( "()(()))" )
        

