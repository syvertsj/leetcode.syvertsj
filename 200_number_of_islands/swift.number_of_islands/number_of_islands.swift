/*
200. Number of Islands
Medium

Add to List

Share
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
*/

import Foundation

class Solution {
    
    var count: Int = 0
    var grid: [[Character]] = [[]]
    var queue: [[Character:Int]] = []
    
    func getTime(_ header: String = "") -> String {
        
        !header.isEmpty ? print(header, terminator: "") : print(terminator: "")
        
        let date = Date()
        let calendar = Calendar.current
        let hour = calendar.component(.hour, from: date)
        let minutes = calendar.component(.minute, from: date)
        let seconds = calendar.component(.second, from: date)
        let nanoseconds = calendar.component(.nanosecond, from: date)
        
        return String(hour) + "." + String(minutes) + "." + String(seconds) + "." + String(nanoseconds)
    }
    
    // print grid
    func printGrid() {
        print("\nInput: ")
        for (r,_) in self.grid.enumerated() {
            for (c,_) in self.grid[r].enumerated() { print(self.grid[r][c], terminator: "") }
            print()
        }
    }
    
    // use depth first search to mark traversed "area" to avoid recounting
    func depthFirstSearch(_ r: Int, _ c: Int, _ numRows: Int, _ numCols: Int) {
        
        // avoid index errors
        guard r > -1 && r < numRows && c > -1 && c < numCols else { return }
        
        // if cell is not "land" (ie: equal to "1") do not bother proceeding
        guard self.grid[r][c] == "1" else { return }
                
        // mark "land" as traversed
        self.grid[r][c] = "X"
        
        // create runtime stack (using recursion) checking the immediate surrounding cells
        depthFirstSearch(r, c - 1, numRows, numCols)
        depthFirstSearch(r, c + 1, numRows, numCols)
        depthFirstSearch(r - 1, c, numRows, numCols)
        depthFirstSearch(r + 1, c, numRows, numCols)
    }
    
    // use breadth first search to mark traversed "area" to avoid recounting
    func breadthFirstSearch(_ r: Int, _ c: Int, _ numRows: Int, _ numCols: Int) {
        
        // if cell is not "land" (ie: equal to "1") do not bother proceeding
        guard self.grid[r][c] == "1" else { return }

        // enqueue current generation cell (as dictionary)
        queue.append(["r": r, "c": c])
        
        while !self.queue.isEmpty {
            let cell = self.queue.remove(at: 0)
            self.grid[cell["r"]!][cell["c"]!] = "X"
            
            // enqueue surrounding cells if they meet criteria: land (value of "1") and within grid
            if r - 1 > -1      && self.grid[r - 1][c] == "1" { breadthFirstSearch(r - 1, c, numRows, numCols) }
            if r + 1 < numRows && self.grid[r + 1][c] == "1" { breadthFirstSearch(r + 1, c, numRows, numCols) }
            if c - 1 > -1      && self.grid[r][c - 1] == "1" { breadthFirstSearch(r, c - 1, numRows, numCols) }
            if c + 1 < numCols && self.grid[r][c + 1] == "1" { breadthFirstSearch(r, c + 1, numRows, numCols) }
        }
    }
    
    // have both dfs and bfs solutions which are being chosen using random number generator (not a requirement)
    func numIslands(_ grid: [[Character]]) -> Int {
        
        self.count = 0
        self.grid = grid
        let randomSelection = Int.random(in: 0...1)
        
        randomSelection == 0 ? print("running DFS implementation") : print("running BFS implementation")
        
        printGrid()
        
        print(self.getTime(" - start time: "))
        
        for r in 0..<self.grid.count {
            for c in 0..<self.grid[r].count {
                if self.grid[r][c] == "1" {
                    self.count += 1
                    randomSelection == 0 ? depthFirstSearch(r, c, self.grid.count, self.grid[r].count) : breadthFirstSearch(r, c, self.grid.count, self.grid[r].count)
                }
            }
        }
        
        print(self.getTime(" - completion time: "))
        
        print("\nOutput: ", terminator: "")
        return count
    }
}

let solution = Solution()
print(solution.numIslands( [["0","0","0","0","0"],["0","0","0","0","0"],["0","0","0","0","0"],["0","0","0","0","0"]] ))
print(solution.numIslands( [["0","0","0","0","0"],["0","0","1","0","0"],["0","0","0","0","0"],["0","0","0","1","0"]] ))
print(solution.numIslands( [["1","0","0","0","0"],["0","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","0"]] ))
print(solution.numIslands( [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]] ))
print(solution.numIslands( [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]] ))
