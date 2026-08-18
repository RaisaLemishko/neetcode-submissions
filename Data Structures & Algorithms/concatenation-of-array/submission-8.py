class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        ans = [] 
        for i in range (2):
            for i, num in enumerate(nums):
                ans.append(num)
        return ans
        