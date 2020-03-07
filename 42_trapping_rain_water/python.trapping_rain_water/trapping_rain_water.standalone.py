#!/usr/bin/env python

# https://leetcode.com/problems/trapping-rain-water/

'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. 
Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''

import sys

class Solution(object):

    # calculate total water accumulation within "structure"
    def trap(self, height):

        if len(height) < 3: return 0
        
        left, right = 0, len(height) - 1     # left and right indices
        lpeak, rpeak, accumulation = 0, 0, 0 # left and right peaks and accumulation
        
        # use convergent indices
        while left < right:

            lpeak = max(height[left], lpeak)
            rpeak = max(height[right], rpeak)

            # only shift left or right index when local peak is the smallest of two sections
            if lpeak < rpeak: 
                accumulation += lpeak - height[left]
                left += 1
            else:
                accumulation += rpeak - height[right]
                right -= 1

        return (height, accumulation)

if __name__ == '__main__':
    solution = Solution()
    import sys
    if len(sys.argv) == 2: 
        print "\nInput: %s \nOutput: %s" % ( solution.trap(sys.argv[1]) )
    else: 
        #print "usage: %s [input array]" % sys.argv[0]
        print "\nInput: %s \nOutput: %s\n" % ( solution.trap([2,0,0,0]) )
        print "\nInput: %s \nOutput: %s\n" % ( solution.trap([2,0,0,2]) )
        print "\nInput: %s \nOutput: %s\n" % ( solution.trap([3,2,1,1]) )
        print "\nInput: %s \nOutput: %s\n" % ( solution.trap([0,2,3]) )
        print "\nInput: %s \nOutput: %s\n" % ( solution.trap([0,1,0,2]) )
        print "\nInput: %s \nOutput: %s\n" % ( solution.trap([2,1,0,1]) )
        print "\nInput: %s \nOutput: %s\n" % ( solution.trap([0,1,0,2]) )
        print "\nInput: %s \nOutput: %s\n" % ( solution.trap([2,1,0,1,3]) )
        print "\nInput: %s \nOutput: %s\n" % ( solution.trap([2,1,0,3,1]) )
        print "\nInput: %s \nOutput: %s\n" % ( solution.trap([2,1,0,1,1]) )
        print "\nInput: %s \nOutput: %s\n" % ( solution.trap([0,1,0,2,0,0,1,3]) )
        print "\nInput: %s \nOutput: %s\n" % ( solution.trap([0,1,0,2,1,0,1,3]) )
        print "\nInput: %s \nOutput: %s\n" % ( solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]) )
        print "\nInput: %s \nOutput: %s\n" % ( solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]) )
        print "\nInput: %s \nOutput: %s\n" % ( solution.trap([5,4,1,2]) )
        print "\nInput: %s \nOutput: %s\n" % ( solution.trap([3,2,3]) )
        print "\nInput: %s \nOutput: %s\n" % ( solution.trap([4,2,3]) )
        print "\nInput: %s \nOutput: %s\n" % ( solution.trap([2,4,3]) )
