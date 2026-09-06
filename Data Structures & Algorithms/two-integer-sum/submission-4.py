class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num in nums:
            for i in range(len(nums)):
                difference = target - nums[i]
                temp = nums[i]
                nums[i] = "X"
                if difference in nums:
                    if not nums.index(difference) == i:
                        return [i, nums.index(difference)]
                else:
                    nums[i] = temp