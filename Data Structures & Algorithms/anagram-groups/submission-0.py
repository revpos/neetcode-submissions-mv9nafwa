class Solution:
    def groupAnagrams(self, A: List[str]) -> List[List[str]]:
        """
        strs is renamed to A, which is the input list of anagram strings
        """
        # key is the first anagram, 
        # values is the list of anagrams that asserts isAnagram(key, A[i])
        groups = dict[str, list[str]]()

        for a in A:
            for key in groups.keys():
                if self.isAnagram(key, a):
                    groups[key].append(a)
                    break
            # in this for-else, 'else' runs only when 'for' loop didn't break
            else:
                groups[a] = [a]

        return list(groups.values())

    # helper function
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = [0] * 26

        for i in range(len(s)):
            counts[ord(s[i]) - ord("a")] += 1
            counts[ord(t[i]) - ord("a")] -= 1

        for c in counts:
            if c != 0:
                return False

        return True
        