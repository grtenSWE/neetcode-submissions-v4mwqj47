#we have a prefix and a suffix list 


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # making prefix and suffix lists

        prefix = [1]*len(nums)
        suffix = [1]*len(nums)
        res = [0] * len(nums)

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
            suffix[i] = suffix[i-1] * nums[len(nums) - i]
           
        for i in range(len(nums)):
            res[i] = prefix[i] * suffix[len(nums) - 1 - i]

        print(prefix)
        print(suffix)

        return res