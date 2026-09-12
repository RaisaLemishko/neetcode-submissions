class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = set()
        for i in range(1, len(nums) + 1):
            res.add(i)
        
        for i in nums:
            if i in res:
                res.remove(i)
        
        return list(res)
        