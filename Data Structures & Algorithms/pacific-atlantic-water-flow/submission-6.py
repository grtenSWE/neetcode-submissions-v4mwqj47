#reverse the problem and run dfs for each cell on the edge. 
#we have 2 sets, on for the pacific and one for pacific and one for Atlantic
#if a cell belongs in both sets then water from it can flow to both oceans

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        directions = [(1,0),(-1,0),(0,-1),(0,1)] #up, down, left, right
        res = []

        m = len(heights)
        n = len(heights[0])

        def dfs(node, visited):
            nonlocal pacific, atlantic, directions, m, n


            stack = deque()
            stack.append(node) #node should be a tuple
            visited.add(node)

            while stack:
                row, col = stack.pop()

                #if next node is equal or higher or if we haven't visit the next node, then add it to the stack, and next is in range

                for delRow, delCol in directions:
                    rowNext = row + delRow
                    colNext = col + delCol
                    if 0 <= rowNext < m and 0 <= colNext < n:
                        if (heights[row][col] <= heights[rowNext][colNext]) and ((rowNext,colNext) not in visited):
                            visited.add((rowNext, colNext))
                            stack.append((rowNext, colNext))

        #we run dfs for the border cells

        for row in range(m):
            dfs((row,0), pacific) #pacific left
            dfs((row,n-1), atlantic) #atlantic right
        for col in range(n):
            dfs((0,col), pacific) #top
            dfs((m-1,col), atlantic) #bottom

        

        res = pacific.intersection(atlantic)
        return list(res)
        
