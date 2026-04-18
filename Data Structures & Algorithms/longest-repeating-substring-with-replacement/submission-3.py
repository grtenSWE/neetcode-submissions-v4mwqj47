
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        maxLen = 0
        maxfreq = 0

        if not s:
            return 0
        elif len(s) == 1:
            return 1

        l = 0
        r = 0

        while r < len(s):
            print(counter)
            #remove the max value, and if the rest sums to more than k 
            #then start moving left index over

            counter[s[r]] = 1 + counter.get(s[r],0)

            maxfreq = max(counter.values()) #this approach is close to the correct one.

            while (r - l + 1) - maxfreq > k:
                counter[s[l]] -= 1
                l += 1
                tmpCounter = list(counter.values())
                tmpCounter.remove(max(tmpCounter))

            maxLen = max(r - l + 1, maxLen)
            r += 1

        return maxLen
                
           
        
