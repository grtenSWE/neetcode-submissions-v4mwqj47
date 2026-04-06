class Solution:
    def numIslands(self, grid) -> int:
        m,n = len(grid), len(grid[0]) #row and col size of grid
        num_island = 0
        directions = ((-1,0),(1,0),(0,1),(0,-1)) #down, right, left. no need to check up. 

        def search(row,col):
            #bfs search
            q = [(row,col)]

            while q:
                row, col = q.pop(0)
                #print(row,col)
                grid[row][col] = "0" #already visited, so it wont be added into the queue again.
                #print(q)
                
                for direction in directions:
                    child_row = row + direction[0]
                    child_col = col + direction[1]

                    if (0 <= child_row < m) and (0 <= child_col < n):
                        if grid[child_row][child_col] == "1":
                            q.append((child_row, child_col))
                        
                        
            

        #checking all indices in the grid
        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1":
                    search(row,col)
                    num_island += 1

        return num_island
        