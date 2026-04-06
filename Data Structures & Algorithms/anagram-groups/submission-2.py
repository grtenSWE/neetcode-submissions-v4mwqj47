

#parse thru each word.

#we want to have a unique ID to each set of words.

#use a hashmap?

#the count of each letter can be the key in a hashmap

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupMap = {}
        for word in strs:
            letters_key = [0] * 26
            for letter in word:
                letters_key[ord(letter)-97] += 1

            if str(letters_key) in groupMap:
                groupMap[str(letters_key)].append(word)
            else:
                groupMap[str(letters_key)] = [word]

        return [groupMap[key] for key in groupMap]
            


        