class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        res = []

        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1

        counterSorted = sorted(counter.items(), key = lambda item:item[1])
        print(counterSorted)
        
        res = counterSorted[-k:]

        for i in range(k):
            res[i] = res[i][0]

        return res
            
