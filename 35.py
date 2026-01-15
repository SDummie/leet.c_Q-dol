class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        
        
        i = 0
        while nums[i] < target and i < len(nums)-1:
            i +=1
        
        if nums[i] < target:
            return len(nums)
        return i