
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #build a dict of the numbers in num and it's next

        if not nums:
            return 0

        seq = set(nums) #could also use a set
        maxSeq = 1

        for num in seq:
            if num - 1 not in seq: #this checks makes it O(n)
                currSeq = 1
                while True:
                    if num + 1 in seq:
                        currSeq += 1
                        num += 1
                    else:
                        maxSeq = max(currSeq, maxSeq)
                        break

        return maxSeq