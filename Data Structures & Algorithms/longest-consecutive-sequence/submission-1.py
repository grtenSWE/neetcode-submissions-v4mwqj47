class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #build a dict of the numbers in num and it's next

        if not nums:
            return 0

        seq = {} #could also use a set

        for num in nums:
            if num not in seq:
                seq[num] = num + 1

        print(seq)
        
        maxSeq = 1

        for num in seq:
            currSeq = 1
            while True:
                if seq[num] in seq:
                    currSeq += 1
                    num = seq[num]
                else:
                    maxSeq = max(currSeq, maxSeq)
                    break

        return maxSeq