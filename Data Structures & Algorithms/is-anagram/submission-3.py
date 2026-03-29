class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    
        # an array to store a char's count increments & decrements
        counts = [0] * 26

        # using ord(word[i]) for the unicode of a char at index i, ord('a') = 97
        for i in range(len(s)):
            counts[ord(s[i]) - ord('a')] += 1
            counts[ord(t[i]) - ord('a')] -= 1
        
        for each in counts:
            if each != 0:
                return False
    
        return True
