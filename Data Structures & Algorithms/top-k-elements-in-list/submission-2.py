#optimal solution

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        freq = [[] for _ in range(len(nums)+1)]
        res = []


        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1

        #still build a hashmap of the numbers and their count
        #but now we use the index as the count and put the number with that count in a list in that index

        for num, count in counter.items():
            freq[count].append(num) #this would be O(n) max

        #now we loop from the end of the freq list until the result list has k elements
        for i in range(len(freq)-1,0,-1):
            if freq[i]:
                for num in freq[i]:
                    res.append(num)
                    if len(res) == k:
                        return res

        

        
        
 

   


            