class Solution(object):
    	
	def depthFirstSearch(self, grid, r, c):
		if r < 0 or c < 0: return
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

		for r in range(0, len(grid)): 
			for c in range(0, len(grid[r])): 
				if grid[r][c] == "1": 
					count += 1
					self.depthFirstSearch(grid, r, c)

		return count 

