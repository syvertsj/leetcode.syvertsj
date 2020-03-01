#!/usr/bin/env python

# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        head = 0; tail = 0; foundchar = {}  # head and tail indices and list for encountered chars
        index = 0; maxm = 0;                # starting index and maximum range for substring

        for head in range(0, len(s)):
            
            if s[head] in foundchar: 
                tail = max(foundchar[s[head]] + 1, tail) # if foundchar[s[head]] + 1 > tail: tail = foundchar[s[head]] + 1

            foundchar[s[head]] = head

            if head + 1 - tail > maxm: 
                maxm = head + 1 - tail; index = tail
        
        explanation = "The answer is %s with length of %s" % (s[index:index + maxm], maxm)

        return (s, maxm, explanation)

if __name__ == '__main__':
    solution = Solution()
    import sys
    if len(sys.argv) == 2: 
        print "\nInput: %s \nOutput: %s\nExplanation: %s" % ( solution.lengthOfLongestSubstring(sys.argv[1]) )
    else: 
        #print "usage: %s [input]" % sys.argv[0]
        print "\nInput: %s \nOutput: %s\nExplanation: %s" % ( solution.lengthOfLongestSubstring("") )
        print "\nInput: %s \nOutput: %s\nExplanation: %s" % ( solution.lengthOfLongestSubstring("abba") )
        print "\nInput: %s \nOutput: %s\nExplanation: %s\n" % ( solution.lengthOfLongestSubstring("pwwkew") )
        print "\nInput: %s \nOutput: %s\nExplanation: %s\n" % ( solution.lengthOfLongestSubstring("dvdf") )
        print "\nInput: %s \nOutput: %s\nExplanation: %s" % ( solution.lengthOfLongestSubstring("abcabcbb") )
        print "\nInput: %s \nOutput: %s\nExplanation: %s" % ( solution.lengthOfLongestSubstring("abcdefghigk") )
