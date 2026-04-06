class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        current = None
        first_idx = 0
        last_idx = len(nums) - 1

        for i, num in enumerate(nums):
            A.append((num,i))

        A.sort()

        while current != target:
            current = A[first_idx][0] + A[last_idx][0]

            if current < target:
                first_idx += 1
            elif current > target:
                last_idx -= 1


        return sorted([A[first_idx][1], A[last_idx][1]])