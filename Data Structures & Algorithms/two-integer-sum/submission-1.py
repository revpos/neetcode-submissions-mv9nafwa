class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = dict()

        for i, n in enumerate(nums):
            complement = target - n

            if complement in hmap:
                return [hmap[complement], i]

            hmap[n] = i
        
        return []

