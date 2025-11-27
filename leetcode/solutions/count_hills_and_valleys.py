class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        prev = nums[0]
        
        for i in range(1, n - 1):
            if nums[i] == prev:
                continue
            
            j = i + 1
            while j < n and nums[j] == nums[i]:
                j += 1
            
            if j == n:
                break
            
            if (nums[i] > prev and nums[i] > nums[j]) or (nums[i] < prev and nums[i] < nums[j]):
                count += 1
            
            prev = nums[i]
        
        return count