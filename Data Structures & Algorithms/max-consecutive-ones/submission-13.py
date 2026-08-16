class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_length, current_length = 0, 0
        
        for num in nums:
            if num == 1:
                current_length += 1
                max_length = max(current_length, max_length)
            else:
                current_length = 0
                
        return max_length
        