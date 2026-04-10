class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        m = (len(nums)-1) // 2
        r = len(nums) - 1

        while l<m:
            if nums[m] < nums[r]: #condition for going left
                r = m
                m = (r + l) // 2
            else:  #condition for going right
                l = m
                m = (r + l) // 2

            print(l)
            print(m)
            print(r)

        return min(nums[m],nums[r])
            