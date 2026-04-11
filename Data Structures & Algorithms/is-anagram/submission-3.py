#trying to improve for space complexity

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = [0]*26

        if len(s) != len(t):
            return False

        for c in s:
            sCount[ord(c) - ord('a')] += 1

        for c in t:
            sCount[ord(c) - ord('a')] -= 1
            if sCount[ord(c) - ord('a')] < 0:
                return False

 
        return True
