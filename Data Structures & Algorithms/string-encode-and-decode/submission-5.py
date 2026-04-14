#save the index to separate the str at the end of the string

class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "''"
        #takes the list

        encode = ""
        sepList = "["

        idx = - 1

        for string in strs[:-1]:
            idx = idx + len(string) + 1 #make sure don't do for last string
            sepList = sepList + " " + str(idx)
            encode = encode + " " + string 

        encode = encode + " " + strs[-1] + f"{sepList}"

        print(encode)

        return encode[1:]

    def decode(self, s: str) -> List[str]:
        if s == "''":
            return []

        sepList = ""
        i = len(s) - 1
        while s[i] != '[':
            sepList = s[i] + sepList 
            i -= 1

        s = s[:i]

        print(s)
        sepList = sepList.split()

        last_i = -1
        decode = []
        for i in sepList:
            i = int(i)
            decode.append(s[last_i+1:i])
            last_i = i

        print(decode)

        print(last_i)

        decode.append(s[last_i+1:])
        
        return decode

