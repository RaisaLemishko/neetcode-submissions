class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        last_not_val_index = 0
        for i, num in enumerate(nums):
            if (num != val):
                nums[last_not_val_index] = num
                last_not_val_index += 1
        return last_not_val_index
