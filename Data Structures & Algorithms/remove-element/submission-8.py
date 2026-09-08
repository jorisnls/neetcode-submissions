class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i in range(len(nums)):
            if val in nums:    
                if nums[i] == val:
                    count+=1
                    nums[i] = None

        for i in range(len(nums)):
            if None in nums:
                nums.remove(None)
        
        nums.sort()
        
        return len(nums)
        