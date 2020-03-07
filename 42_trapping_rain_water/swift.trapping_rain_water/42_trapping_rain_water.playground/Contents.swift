
class Solution {
    
    func trap(_ height: [Int]) -> ([Int], Int) {
     
        guard height.count > 2 else { return (height, 0) }
        
        var left = 0, right = height.count - 1      // left and right indices
        var accumulation = 0, lpeak = 0, rpeak = 0  // left and right peaks and accumulation
        
        while left < right {
            
            lpeak = max(height[left],  lpeak)
            rpeak = max(height[right], rpeak)
            
            // only shift an index if it's local peak is the smaller of the two halves
            if lpeak < rpeak {
                accumulation += lpeak - height[left]
                left += 1
            } else {
                accumulation += rpeak - height[right]
                right -= 1
            }
        }
        
        return (height, accumulation)
    }
}

let solution = Solution()
print("\nInput: ", solution.trap([2,0,0,0]).0, "\nOutput: ", solution.trap([2,0,0,0]).1)
print("\nInput: ", solution.trap([2,0,0,2]).0, "\nOutput: ", solution.trap([2,0,0,2]).1)
print("\nInput: ", solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]).0, "\nOutput: ", solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]).1)
print("\nInput: ", solution.trap([5,4,1,2]).0, "\nOutput: ", solution.trap([5,4,1,2]).1)
print("\nInput: ", solution.trap([3,2,3]).0, "\nOutput: ", solution.trap([3,2,3]).1)
print("\nInput: ", solution.trap([4,2,3]).0, "\nOutput: ", solution.trap([4,2,3]).1)
print("\nInput: ", solution.trap([2,4,3]).0, "\nOutput: ", solution.trap([2,4,3]).1)
