class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_idx_map = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in num_idx_map:
                return [num_idx_map[complement], i]

            num_idx_map[nums[i]] = i
        
        return []

