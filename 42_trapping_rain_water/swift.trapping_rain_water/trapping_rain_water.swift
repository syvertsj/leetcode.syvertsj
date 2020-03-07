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
            if lpeak <= rpeak: 
                accumulation += lpeak - height[left]
                left += 1
            else:
                accumulation += rpeak - height[right]
                right -= 1
            
        return accumulation

