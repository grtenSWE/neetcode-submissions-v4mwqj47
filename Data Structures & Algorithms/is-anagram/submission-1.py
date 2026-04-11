class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = [0]*26
        tCount = [0]*26

        if len(s) != len(t):
            return False

        for c in s:
            sCount[ord(c) - ord('a')] += 1

        for c in t:
            tCount[ord(c) - ord('a')] += 1

        print(sCount)
        print(tCount)
        return sCount == tCount

            