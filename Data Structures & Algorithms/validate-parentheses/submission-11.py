#first and last index are of the same bracket type.
#slides into the middle
#only even length is valid

#how to compare two brackets?
# - 

#Steps to solve a leetcode problem

#understand
#consider all (many) test cases
#come up with solution, or bruteforce to start of with
#write down solution on paper/laptop
#write solution

class Solution:
    def isValid(self, s: str) -> bool:
        openBrackets = ['(','[','{']
        completeBrackets = ['()','[]','{}']
        stack = []

        if len(s) % 2 != 0:
            return False
        
        for bracket in s:
            if bracket in openBrackets:
                stack.append(bracket)
            else: 
                if not stack or stack[-1] + bracket not in completeBrackets:
                    return False
                stack.pop()

       
        return True if not stack else False


        