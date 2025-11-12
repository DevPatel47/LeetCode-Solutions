class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hashmap = {}
        for i in range(0,n):
            remaining = target - nums[i]
            if remaining in hashmap:
                return [hashmap[remaining],i]
            hashmap[nums[i]] = i