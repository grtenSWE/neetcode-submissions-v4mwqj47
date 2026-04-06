import numpy as np

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        current = None
        first_idx = 0
        last_idx = len(nums) - 1

        sorted_indices = np.argsort(nums)

        while current != target:
            current = nums[sorted_indices[first_idx]] + nums[sorted_indices[last_idx]]

            if current < target:
                first_idx += 1
            elif current > target:
                last_idx -= 1


        return sorted([int(sorted_indices[first_idx]), int(sorted_indices[last_idx])])