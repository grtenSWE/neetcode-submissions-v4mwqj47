#recursive solution.

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #sort nums once

        nums.sort()
        res = []

        #pass through the solution to get it's count for each number
        #check if this exact count is already in the List

        combs = [] #dict of dict

        def combSum(target, currentSol):
            #base case
            if target == 0:
                print(currentSol) 
                #we need to also check if this is a unique combination
                
                res.append(currentSol[1:])


            for num in nums:
                #print(currentSol)
                #print(num)
                #print("____")
                if num <= target and currentSol[-1] <= num:
                    curr = currentSol.copy()
                    curr.append(num)
                    combSum(target-num, curr)
                

                

        combSum(target, [0])
        return res

                    
        
    
        