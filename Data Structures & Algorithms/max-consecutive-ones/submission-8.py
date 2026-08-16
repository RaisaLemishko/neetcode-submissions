class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_length = 0
        sublist = []
        for i, num in enumerate(nums):
            if num == 1:
                sublist.append(num)
                if len(sublist) > max_length:
                    max_length = len(sublist)
            else:
                sublist = []
                
        return max_length
        