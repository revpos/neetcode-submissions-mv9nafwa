from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # defaultdict(list) automatically creates a new empty list if a key doesn't exist yet
        groups = defaultdict(list)

        for word in strs:
            # mutual sorted key for all anagram words
            sorted_key = "".join(sorted(word))
            
            # directly appending the word without verifying the group/key existence
            # as the new list value creation logic is auto-handled by defaultdict
            groups[sorted_key].append(word)

        return list(groups.values())