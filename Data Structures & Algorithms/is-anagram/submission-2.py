class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    
        counts = [c for c in s] 

        for c in t:
            if c in counts:
                counts.remove(c)
        
        return len(counts) == 0       
        
         