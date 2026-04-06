#best solution

#use a hashmap to map the closing to the opening
#so we can check if the value at the index matches with the stack pop


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairMap = {')':'(', '}':'{', ']':'['}

        for bracket in s:
            if bracket in pairMap: #if its a closing bracket
                if stack and stack[-1] != pairMap[bracket]:
                    return False
                elif not stack:
                    return False
                else:
                    stack.pop()
                
            else:
                stack.append(bracket)

        return True if not stack else False


        