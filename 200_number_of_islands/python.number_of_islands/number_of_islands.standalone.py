#!/usr/bin/env python

# https://leetcode.com/problems/number-of-islands/

'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
'''

class Solution(object):

	def print_grid(self, grid):
		for i, r in enumerate(grid): 
			for j, c in enumerate(r): print grid[i][j],
			print 

	# traverse areas around island and mark as traversed
	def depthFirstSearch(self, grid, r, c):
		try:
			if grid[r][c] != "1": return
			grid[r][c] = "X"
			self.depthFirstSearch(grid, r - 1, c) 
			self.depthFirstSearch(grid, r + 1, c) 
			self.depthFirstSearch(grid, r, c - 1) 
			self.depthFirstSearch(grid, r, c + 1) 
		except IndexError:
			return

	def numIslands(self, grid):
		"""
		:type grid: List[List[str]]
		:rtype: int
		"""
		count = 0

		print "\nInput: "; self.print_grid(grid)

		for r in range(0, len(grid)): 
			for c in range(0, len(grid[r])): 
				if grid[r][c] == "1": 
					count += 1
					self.depthFirstSearch(grid, r, c)

		return count

if __name__ == '__main__':
    solution = Solution()
    import sys
    if len(sys.argv) == 2: 
        print "\nInput: %s \nOutput: %s" % ( solution.numIslands(sys.argv[1]) )
    else: 
        #print "usage: %s [input]" % sys.argv[0]
        print "\nOutput: %s" % ( solution.numIslands( [["0","0","0","0","0"],["0","0","0","0","0"],["0","0","0","0","0"],["0","0","0","0","0"]] ) )
        print "\nOutput: %s" % ( solution.numIslands( [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]] ) )
        print "\nOutput: %s" % ( solution.numIslands( [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]] ) )
