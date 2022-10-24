class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s) 
        
        for idx, char in enumerate(s):
            if count[char] == 1:
                return idx
        return -1