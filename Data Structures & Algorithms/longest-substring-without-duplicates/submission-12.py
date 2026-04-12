#have a dictionary that keeps count of all the char that appeared so far


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0

        if not s:
            return 0
        else:  
            longest = 1

        count = {}
        count[s[l]] = 0 #we save the index of the occurrent of this character

        for r in range(1,len(s)):
            #print(count)
            if s[r] in count:
                l = max(count[s[r]] + 1, l) 
           
            longest = max(longest, (r - l) + 1) #why is moving this outside the else condition a good idea?
            count[s[r]] = r


        return longest

