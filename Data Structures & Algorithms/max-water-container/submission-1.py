#two l and r pointer in opposite ends
#we want to keep the highest height out of the 2
#so we move the lowest one
#keep best result 

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        volMax = 0

        while l<r:
            vol = min(heights[l],heights[r]) * (r - l)

            if vol > volMax:
                volMax = vol

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
            

        return volMax