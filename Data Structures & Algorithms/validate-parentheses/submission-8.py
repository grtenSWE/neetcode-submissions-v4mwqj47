#first and last index are of the same bracket type.
#slides into the middle
#only even length is valid

#how to compare two brackets?
# - 



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
                if len(stack) == 0:
                    return False
                openBracket = stack.pop()
                if openBracket + bracket not in completeBrackets:
                    return False

        if len(stack) > 0:
            return False
        return True


        