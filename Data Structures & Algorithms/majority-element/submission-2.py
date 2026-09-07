class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        majority = nums[math.floor(len(nums)/2)]
        return majority



        