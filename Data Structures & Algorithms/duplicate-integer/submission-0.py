class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tracker = {}

        for num in nums:
            if num in tracker:
                return True
            else:
                tracker[num] = None

        return False