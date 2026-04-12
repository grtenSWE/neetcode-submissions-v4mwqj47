class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 1

        if not s:
            return 0
        else:  
            longest = 1

        count = {} #count now stores the count of that char, not index
        count[s[l]] = 1
        

        while r < len(s):
            #print(count)
            
            if count.get(s[r],0) == 1:
                print(l)
                print(r)
                print(count.get(s[r],0))
                print(count)
            
                count[s[l]] = 0
                l += 1
            
            else:    
                longest = max(longest, (r - l) + 1)
                print(f"longest: {longest}")
                count[s[r]] = 1
                r += 1
                
            
          


        return longest