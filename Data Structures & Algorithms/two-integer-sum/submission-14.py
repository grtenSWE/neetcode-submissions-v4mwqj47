#Hashmap implementation

#build a hashmap that that contains val : idx
#check if the complement of current number 
#is in the hashmap, if yes, get the idx and return.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, num in enumerate(nums):
            comp = target - num
            if comp in prevMap:
                return sorted([i,prevMap[comp]])
            else:
                prevMap[num] = i

        return []

        