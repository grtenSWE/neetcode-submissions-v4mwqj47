class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        m = (len(nums)-1) // 2
        r = len(nums)-1
        while l < m:
            if nums[l] < nums[m]:
                if nums[l] <= target <= nums[m]:
                    r = m
                else:
                    l = m + 1
            else:
                if nums[m] <= target <= nums[r]:
                    l = m
                else:
                    r = m - 1
            m = (l + r) // 2
            
            
        if nums[m] == target:
            return m
        elif nums[r] == target:
            return r
        else:
            return -1

  