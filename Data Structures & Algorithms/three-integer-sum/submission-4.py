#sort the list of numbers (nlogn)
#use 2 pointers to check sum
#check on the right of pointer if sum is less than or qual to zero
#check on the left if sum is more than 0

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]: #skipping duplicates
                continue
            l = i + 1 #left is one to the left of fixed 
            r = len(nums) - 1 #right starts from end of nums
            
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    triplets.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return triplets