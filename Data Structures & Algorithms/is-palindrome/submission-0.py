#palindrome is when a word is the same when reversed.
#case insensitive, also spacing doesn't matter. 

#need a way to only consider alphanumeric chars.
#then use two pointers to check if each comparison is the same.

#use char.isalnum()

class Solution:
    def isPalindrome(self, s: str) -> bool:
        sAlnum = ""
        for c in s:
            if c.isalnum():
                sAlnum = sAlnum + c.lower()


        for i in range(len(sAlnum)//2):
            j = len(sAlnum) - i - 1
            if sAlnum[i] != sAlnum[j]:
                return False

        return True
        